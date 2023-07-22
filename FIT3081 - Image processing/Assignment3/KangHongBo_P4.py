import cv2
import numpy as np
from scipy.signal import convolve2d
from skimage.util import random_noise
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


def Load_Weights_Bias(filename="KangHongBo_Exp1_Weights.txt.npz"):
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
    #gaussian noise standard variation = 1
    noise_img_gaussian=random_noise(file,mode='gaussian',var=1,seed=4)
    file = noise_img_gaussian
    #show image
    # cv2.imshow("img",file)
    # cv2.waitKey(0)
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