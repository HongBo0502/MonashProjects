import numpy as np
import cv2
import os
from scipy.signal import convolve2d
class Neural_Network:
    def __init__(self,Input_Neurons, Hidden_Neurons, Output_Neurons):
        """
        Step 1: Initialization of the Weights and Biases
        Initializing of the Weights. Random float number between -0.5 to 0.5 for weights.
        """
        text=open("KangHong\Seed Number.txt","r")
        seed=int(text.read())
        np.random.seed(seed)
        text.close()
        self.wji= np.random.uniform(-0.5, 0.5, size=(Hidden_Neurons, Input_Neurons))
        self.wkj = np.random.uniform(-0.5, 0.5, size=(Output_Neurons, Hidden_Neurons))
        self.bias_j = np.random.uniform(0, 1, size=(Hidden_Neurons, 1))
        self.bias_k = np.random.uniform(0, 1, size=(Output_Neurons, 1))

    def Read_Files(self):
        """
        Step 2: Reading of Training Files, and Target Files
        """
        training_files = []
        outputs = []
        for i in range(8):
            j=i+1
            count=1
            while j <=120:
                # print(j)
                #read file
                file = cv2.imread("KangHong/Train/Img " + "(" + str(j) + ").jpg")
                #convert file to 2d array
                file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
                #resize to 16
                reshaped_image = file.reshape(4,7, 4,7)

                # Apply max pooling to resize the image to 49x49
                file = reshaped_image.mean(axis=(3, 1))
                # cv2.imwrite("KangHong/Exp/Img " + "(" + str(j) + ").jpg",file)

                # print(str(file) +"\n")
                #prepare kernels - Sobel
                kernel_x = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
                kernel_y = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
                #apply kernels
                img_x = convolve2d(file, kernel_x, mode='same')
                img_y = convolve2d(file, kernel_y, mode='same')
                G=np.sqrt(img_x**2 + img_y**2)
                #clip values to 0-255
                G = np.clip(G, 0, 255)
                # print(G)
                threshold = np.percentile(G,75)
                # print("threshold= " + str(threshold))
                G[G < threshold] = 0
                #if more than threshold 
                G[G >= threshold] = 1
                # cv2.imwrite("KangHong/Exp_2/Img " + "(" + str(j) + ").jpg",G)
                #append to training files
                # print(G)
                training_files.append(np.array(G).flatten())
                #one hot encode the outputs
                j+=8
                # print("count= " + str(count))
                outputs.append(np.eye(15)[(count-1)%15])
                count+=1
                
        return training_files, outputs

   
    def Forward_Input_Hidden(self,input_layer):
        """
        Step 3: Forward Propagation from Input -> Hidden Layer.
        Obtain the results at each neuron in the hidden layer.
        Calculate 𝑁𝑒𝑡_𝑗 and 𝑂𝑢𝑡_𝑗
        """
        # Calculate Net_j
        self.net_j = np.dot(self.wji, input_layer)
        # Calculate Out_j using an activation function like sigmoid
        self.out_j = 1/(1 + np.exp(-self.net_j - self.bias_j))

    
    def Forward_Hidden_Output(self):
        """
        Step 4: Forward Propagation from Hidden -> Output Layer.
        Forward Propagation from Hidden -> Output Layer.
        Calculate 𝑁𝑒𝑡_𝑘 and 𝑂𝑢𝑡_𝑘
        """
        # Calculate Net_k
        self.net_k = np.dot(self.wkj, self.out_j)
        # Calculate Out_k using an activation function like sigmoid
        self.out_k = 1/(1 + np.exp(-self.net_k - self.bias_k))

    
    def Error_Function(self,outputs):
        """
        Step 5: Check for the global error or number of iterations.
        """
        out_k = self.out_k.flatten()
        outputs = outputs.flatten()
        # Calculate the total error.
        Error = 0.5 * (outputs - out_k) ** 2
        return np.sum(Error)

    
    def Check_for_End(E_total, num_iterations, threshold=0.001, max_iterations=1000):
        """
        Check whether the total error is less than the error set by the user or the number of iterations is reached.
        returns true or false
        """
        return E_total < threshold or num_iterations > max_iterations

   
    def Weight_Bias_Correction_Output(self, outputs, learning_rate=0.01):
        """
        Step 6: Correction of Weights and Biases between Hidden and Output Layer.
        Calculate 𝑑𝑤𝑘𝑘𝑗 and 𝑑𝑏𝑘𝑘𝑗
        """
        # Calculating Correction of Weights between Hidden and Output Layer.
        self.delta_Etotal_Outk = -(outputs - self.out_k)
        self.delta_outk_Netk = self.out_k * (1 - self.out_k)
        self.delta_Netk_Wkj = np.tile(self.out_j.T, (len(self.wkj), 1))  # repeat out_j along rows
        self.dw_kj = learning_rate * self.delta_Etotal_Outk * self.delta_outk_Netk * self.delta_Netk_Wkj

        #To be used for calculation in the next step
        self.delta_k = self.delta_Etotal_Outk * self.delta_outk_Netk

        # Calculating Correction of Bias between Hidden and Output Layer
        self.db_k = learning_rate * self.delta_k

    
    def Weight_Bias_Correction_Hidden(self, inputs, learning_rate=0.01):
        """
        Step 7: Correction of Weights and Biases between Input and Hidden Layer.
        Calculate 𝑑𝑤𝑗𝑗𝑖 and 𝑑𝑏𝑗𝑗𝑖
        """
        # Calculating Correction of Weights and Bias between Input and Hidden Layer.
        self.delta_Etotal_Outj = np.dot(self.wkj.T, self.delta_k)
        self.delta_outj_Netj = self.out_j * (1 - self.out_j)
        self.delta_Netj_Wji = np.tile(inputs.T, (len(self.wji), 1))  # repeat inputs along rows
        self.dw_ji = learning_rate * self.delta_Etotal_Outj * self.delta_outj_Netj * self.delta_Netj_Wji

        # Calculating Correction of Bias between Hidden and Output Layer
        self.db_j = learning_rate * self.delta_Etotal_Outj * self.delta_outj_Netj

    
    def Weight_Bias_Update(self):
        """
        Step 8: Update the Weights and Biases
        Calculate 𝑤𝑘𝑘𝑗+ and 𝑏𝑘𝑘𝑗+
        Calculate 𝑤𝑗𝑗𝑖+ and 𝑏𝑗𝑗𝑖+
        """
        # Calculate 𝑤𝑘_𝑘𝑗+ and 𝑏𝑘_𝑘𝑗+
        self.wkj -= self.dw_kj
        self.bias_k -= self.db_k

        # Calculate 𝑤𝑗_𝑗𝑖+ and 𝑏𝑗_𝑗𝑖+
        self.wji -= self.dw_ji
        self.bias_j -= self.db_j


    def Saving_Weights_Bias(self,filename="KangHongBo_Exp3_Weights.txt"):
        """
        Step 10: Save the Weights and Biases
        Save 𝑤𝑘_𝑘𝑗 and 𝑏𝑘_𝑘𝑗
        Save 𝑤𝑗_𝑗𝑖 and 𝑏𝑗_𝑗𝑖
        """
        np.savez(filename, wji=self.wji, wkj=self.wkj, bias_j=self.bias_j, bias_k=self.bias_k)


    """
    Training the Neural Network
    """
    def Training_Neural_Network(self, inputs, outputs,learn_rate=0.01):
        E_total = 0
        for i in range(len(inputs)):
            inp=np.reshape(inputs[i],(len(inputs[i]),1))
            out=np.reshape(outputs[i],(len(outputs[i]),1))

            
            self.Forward_Input_Hidden(inp)
            self.Forward_Hidden_Output()
            E_total += self.Error_Function(out)
                
            self.Weight_Bias_Correction_Output(out, learn_rate)
            self.Weight_Bias_Correction_Hidden(inp, learn_rate)
            self.Weight_Bias_Update() 
        self.Saving_Weights_Bias()

        return E_total

if __name__ == "__main__":
    nn=Neural_Network(16,10,15)
    inputs, outputs = nn.Read_Files()
    epochs = 1000
    threshold = 0.001
    for i in range(epochs):
        E_total = nn.Training_Neural_Network(inputs, outputs,learn_rate=1.5)
        print("Total Error: " + str(E_total) + " | Epoch: " + str(i+1))
        # if E_total < threshold:
        #     print("Complete")
        #     break

"""
Testing the Neural Network
"""
import cv2
import numpy as np
from scipy.signal import convolve2d

def Forward_Input_Hidden(input_layer, wji, bias_j):
    # Forward Propagation from Input -> Hidden Layer.
    # Obtain the results at each neuron in the hidden layer.
    # Calculate 𝑁𝑒𝑡_𝑗 and 𝑂𝑢𝑡_𝑗
    net_j = np.zeros_like(bias_j)
    out_j = np.zeros_like(bias_j)

    for j in range(len(net_j)):
        for i in range(len(input_layer)):
            net_j[j] += wji[j][i] * input_layer[i]

    out_j = 1 / (1 + np.exp(-(net_j + bias_j)))

    return net_j, out_j

def Forward_Hidden_Output(out_j, wkj, bias_k):
    # Forward Propagation from Hidden -> Output Layer.
    # Calculate 𝑁𝑒𝑡_𝑘 and 𝑂𝑢𝑡_𝑘
    net_k = np.zeros_like(bias_k)
    out_k = np.zeros_like(bias_k)

    for k in range(len(net_k)):
        for j in range(len(out_j)):
            net_k[k] += wkj[k][j] * out_j[j]

    out_k = 1 / (1 + np.exp(-(net_k + bias_k)))

    return net_k, out_k


def Load_Weights_Bias(filename="KangHongBo_Exp3_Weights.txt.npz"):
    # Load the weights and bias from the file
    # The weights and bias are saved in a dictionary
    # The dictionary is saved in a .npz file
    # The dictionary contains the following keys:
    # wji, wkj, bias_j, bias_k
    # The values of each key is a numpy array
    data = np.load(filename)
    wji = data['wji']
    wkj = data['wkj']
    bias_j = data['bias_j']
    bias_k = data['bias_k']

    return wji, wkj, bias_j, bias_k

# Load the weights and bias
wji, wkj, bias_j, bias_k = Load_Weights_Bias()


# Testing the Neural Network
dictionary = [2,3,4,7,9,'A','E','I','J','L','O','P','T','W','X']
outputs = []
outk = []
for i in range(1,31):
    #read file
    file = cv2.imread("KangHong/Test/Img ("  + str(i) + ").jpg")
    #convert file to 2d array
    file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
    #resize to 49
    # file = cv2.resize(file,(4,4))
    reshaped_image = file.reshape(4,7, 4,7)

    # Apply max pooling to resize the image to 49x49
    file = reshaped_image.mean(axis=(3, 1))
    # print(str(file) +"\n")
    #prepare kernels - Sobel
    kernel_x = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    kernel_y = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    #apply kernels
    img_x = convolve2d(file, kernel_x, mode='same')
    img_y = convolve2d(file, kernel_y, mode='same')
    G=np.sqrt(img_x**2 + img_y**2)
    
    #clip values to 0-255
    G = np.clip(G, 0, 255)
    # print(G)
    threshold = np.percentile(G,75)
    # print("threshold= " + str(threshold))
    G[G < threshold] = 0
    #if more than threshold 
    G[G >= threshold] = 1
    
    file = np.array(G).flatten()
    
    net_j, out_j = Forward_Input_Hidden(file, wji, bias_j)
    net_k, out_k = Forward_Hidden_Output(out_j, wkj, bias_k)
    
    for k in range(len(out_k)):
        if out_k[k] == max(out_k):
            outputs.append(dictionary[k])
            outk.append(out_k[k])

ans = [2,2,3,3,4,4,7,7,9,9,'A','A','E','E','I','I','J','J','L','L','O','O','P','P','T','T','W','W','X','X']
dic=['i','j','i','j','i','j','i','j','i','j','9',"10",'9',"10",'9',"10",'9',"10",'9',"10",'9',"10",'9',"10",'9',"10",'9',"10",'9',"10"]
# print(outputs)
# print(outk)
# print(len(outputs))
# print(len(outk))
count = 0
for i in range(len(ans)):
    if ans[i] == outputs[i]:
        print("Img (" + str(i+1) + ").jpg: " + str(outputs[i]) + str(outk[i])+" - Correct")
        print(str(ans[(i)]) + dic[i] + str(outk[i]))
        count += 1

print(count)
print("Accuracy: ", count/len(ans))