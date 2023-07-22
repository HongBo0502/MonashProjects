import "./style.css";
import { interval, fromEvent,merge} from "rxjs";
import { map, filter, scan } from "rxjs/operators";
function main() {
  /**
   * Inside this function you will use the classes and functions from rx.js
   * to add visuals to the svg element in pong.html, animate them, and make them interactive.
   *
   * Study and complete the tasks in observable examples first to get ideas.
   *
   * Course Notes showing Asteroids in FRP: https://tgdwyer.github.io/asteroids/
   *
   * You will be marked on your functional programming style
   * as well as the functionality that you implement.
   *
   * Document your key!
   */

  /**
   * This is the view for your game to add and update your game elements.
   */
  const svg = document.getElementById("svgCanvas")!
  const bg = document.getElementById("backgroundLayer")!
  const fg=document.getElementById("foregroundLayer")!
  const txt=document.getElementById("textLayer")!
  // reference from asteroid code
    const attr = (e:Element,o:{ [key:string]: Object }) =>
    { for(const k in o) e.setAttribute(k,String(o[k])) }
  //take in the updated state and change the previous state
    function updateView(state:State): void {
      const 
      updateBodyView=(b:Body)=>{
        function createBodyView(){
          const v = document.createElementNS(bg.namespaceURI,'rect')!;
          attr(v,{id:b.id,height:b.height,width:b.width,transform:`translate(${b.posx},${b.posy})`});

          v.classList.add(b.viewType)
          bg.appendChild(v)
          return v;
        }
        const v=document.getElementById(b.id)||createBodyView();
        attr(v,{transform:`translate(${b.posx},${b.posy})`});
      },
      updatefrog=(b:Body)=>{
        function createBodyView(){
          const v = document.createElementNS(bg.namespaceURI,'rect')!;
          attr(v,{id:b.id,height:b.height,width:b.width,transform:`translate(${b.posx},${b.posy})`});

          v.classList.add(b.viewType)
          fg.appendChild(v)
          return v;}
        const x=document.getElementById(b.id)||createBodyView()
        attr(x,{transform:`translate(${b.posx},${b.posy})`});
      }
      updatefrog(state.frog);
      state.cars1.forEach(updateBodyView);
      state.cars2.forEach(updateBodyView);
      state.cars3.forEach(updateBodyView);
      state.cars4.forEach(updateBodyView);
      state.logs1.forEach(updateBodyView);
      state.logs2.forEach(updateBodyView);
      state.logs3.forEach(updateBodyView);
      state.logs4.forEach(updateBodyView);
      state.Goal.forEach(updateBodyView);
      state.Croc.forEach(updateBodyView);
      if (state.gameover) {
        const v=document.getElementById('text')!
        v.textContent = 'Game Over';
        const sc=document.getElementById('HighScore')!
        sc.textContent='HighScore: '+state.HighScore
      }
      else{
        const v=document.getElementById('text')!||createTextView()
        function createTextView(){
        const v =document.createElementNS(svg.namespaceURI, 'text')!;
        attr(v, {
          id: 'text',
          x: Constants.CanvasSize / 6,
          y: Constants.CanvasSize / 2,
          class: 'gameover',
        });
        v.textContent=''
        txt.appendChild(v);
      }
      const x=document.getElementById('text')!
      
      const text=x.textContent!
          if(text.length>0){
          txt.textContent=''
        }
    
      }
      
    
      if(state.restart){
        const scoreBoard=document.getElementById('score')!  
        scoreBoard.textContent="Score: 0"
      }
      if(state.isScore){
        const scoreBoard=document.getElementById('score')!
        scoreBoard.textContent="Score: "+state.Score
      }
    }

    type ViewType = 'frog' | 'cars' | 'log' |'goal'|'croc'
    type obstacles = Readonly<{posx:number,posy:number,height:number,width:number,velocity:number}>
    type ObjectId = Readonly<{id:string,createTime:number}>
    interface IBody extends obstacles, ObjectId {
      viewType: ViewType,
    }
    type Body = Readonly<IBody>

    type State = Readonly<{
      time:number;
      frog:Body;
      cars1:ReadonlyArray<Body>
      cars2:ReadonlyArray<Body>
      cars3:ReadonlyArray<Body>
      cars4:ReadonlyArray<Body>
      logs1:ReadonlyArray<Body>
      logs2:ReadonlyArray<Body>
      logs3:ReadonlyArray<Body>
      logs4:ReadonlyArray<Body>
      Goal:ReadonlyArray<Body>
      Croc:ReadonlyArray<Body>
      isScore:boolean
      Score:number
      HighScore:number
      TOS:number
      gameover:boolean
      restart:boolean
    }>
    function createFrog():Body{
      return {
        id: 'frog',
        viewType:'frog',
        posx:288,
        posy:576,
        height:24,
        width:24,
        velocity:0,
        createTime:0
      }
    }
    const 
    Constants = {
      CanvasSize: 600,
      StartCarsCount1: 3,
      StartCarsCount2:3,
      StartCarsCount3:4,
      StartCarsCount4:3,
      StartLogsCount1:3,
      StartLogsCount2:4,
      StartLogsCount3:3,
      StartLogsCount4:3,
      StartTime: 0,
      CarsLoc1:[{posx:570,posy:552,width:30,height:24,velocity:1},{posx:220,posy:552,width:100,height:24,velocity:1},{posx:80,posy:552,width:50,height:24,velocity:1}],
      CarsLoc2:[{posx:500,posy:528,width:25,height:24,velocity:-0.5},{posx:300,posy:528,width:90,height:24,velocity:-0.5},{posx:20,posy:528,width:150,height:24,velocity:-0.5}],
      CarsLoc3:[{posx:5,posy:504,width:25,height:24,velocity:0.8},{posx:100,posy:504,width:30,height:24,velocity:0.8},{posx:345,posy:504,width:60,height:24,velocity:0.8},{posx:465,posy:504,width:50,height:24,velocity:0.8}],
      CarsLoc4:[{posx:33,posy:480,width:30,height:24,velocity:-0.3},{posx:200,posy:480,width:70,height:24,velocity:-0.3},{posx:400,posy:480,width:100,height:24,velocity:-0.3}],
      LogsLoc1:[{posx:500,posy:432,width:60,height:24,velocity:0.6},{posx:300,posy:432,width:90,height:24,velocity:0.6},{posx:20,posy:432,width:50,height:24,velocity:0.6},{posx:90,posy:432,width:150,height:24,velocity:0.6}],
      LogsLoc2:[{posx:5,posy:408,width:70,height:24,velocity:-0.9},{posx:180,posy:408,width:60,height:24,velocity:-0.9},{posx:345,posy:408,width:60,height:24,velocity:-0.9},{posx:465,posy:408,width:50,height:24,velocity:-0.9}],
      LogsLoc3:[{posx:530,posy:384,width:70,height:24,velocity:0.7},{posx:280,posy:384,width:100,height:24,velocity:0.7},{posx:80,posy:384,width:50,height:24,velocity:0.7}],
      LogsLoc4:[{posx:530,posy:360,width:70,height:24,velocity:-0.5},{posx:280,posy:360,width:100,height:24,velocity:-0.5},{posx:80,posy:360,width:50,height:24,velocity:-0.5}],
      crocLoc:[{posx:70,posy:336,width:90,height:24,velocity:-0.8},{posx:330,posy:336,width:100,height:24,velocity:-0.8},{posx:460,posy:336,width:70,height:24,velocity:-0.8}],
      crocCount:3,
      GoalCount:5,
      Goals:[{posx:96,posy:312,width:24,height:24,velocity:0},{posx:192,posy:312,width:24,height:24,velocity:0},{posx:288,posy:312,width:24,height:24,velocity:0},{posx:384,posy:312,width:24,height:24,velocity:0},{posx:480,posy:312,width:24,height:24,velocity:0}],
    } as const
    const 
    createRect=(viewType: ViewType)=> (oid:ObjectId)=>(obj:obstacles)=><Body>{
      ...oid,
      ...obj,
      id:viewType+oid.id,
      viewType:viewType
    },
    createCar=createRect('cars'), 
    createLog=createRect('log'),
    creategoal=createRect('goal'),
    createCroc=createRect('croc')
    // creating the object save into the state
    const startcarR1=[...Array(Constants.StartCarsCount1)].map((_,i)=>
    createCar({id:String(i),createTime:Constants.StartTime})(Constants.CarsLoc1[i]))
    const startcarR2=[...Array(Constants.StartCarsCount2)].map((_,i)=>
    createCar({id:String(i+Constants.StartCarsCount1),createTime:Constants.StartTime})(Constants.CarsLoc2[i]))
    const startcarR3=[...Array(Constants.StartCarsCount3)].map((_,i)=>
    createCar({id:String(i+Constants.StartCarsCount1+Constants.StartCarsCount2),createTime:Constants.StartTime})(Constants.CarsLoc3[i]))
    const startcarR4=[...Array(Constants.StartCarsCount4)].map((_,i)=>
    createCar({id:String(i+Constants.StartCarsCount1+Constants.StartCarsCount2+Constants.StartCarsCount3),createTime:Constants.StartTime})(Constants.CarsLoc4[i]))
    const startlogR1=[...Array(Constants.StartCarsCount1)].map((_,i)=>
    createLog({id:String(i),createTime:Constants.StartTime})(Constants.LogsLoc1[i]))
    const startlogR2=[...Array(Constants.StartLogsCount2)].map((_,i)=>
    createLog({id:String(i+Constants.StartLogsCount1),createTime:Constants.StartTime})(Constants.LogsLoc2[i]))
    const startlogR3=[...Array(Constants.StartLogsCount3)].map((_,i)=>
    createLog({id:String(i+Constants.StartLogsCount1+Constants.StartLogsCount2),createTime:Constants.StartTime})(Constants.LogsLoc3[i]))
    const startlogR4=[...Array(Constants.StartLogsCount4)].map((_,i)=>
    createLog({id:String(i+Constants.StartLogsCount1+Constants.StartLogsCount2+Constants.StartLogsCount3),createTime:Constants.StartTime})(Constants.LogsLoc4[i]))
    const startgoal=[...Array(Constants.GoalCount)].map((_,i)=>
    creategoal({id:String(i),createTime:Constants.StartTime})(Constants.Goals[i]))
    const startCroc=[...Array(Constants.crocCount)].map((_,i)=>
    createCroc({id:String(i),createTime:Constants.StartTime})(Constants.crocLoc[i]))
    
    const initialState: State = { 
      time:0,
      frog:createFrog(),
      cars1:startcarR1,
      cars2:startcarR2,
      cars3:startcarR3,
      cars4:startcarR4,
      logs1:startlogR1,
      logs2:startlogR2,
      logs3:startlogR3,
      logs4:startlogR4,
      Goal:startgoal,
      Croc:startCroc,
      isScore:false,
      Score:0,
      TOS:0,
      HighScore:0,
      gameover:false,
      restart:false
    }
    const s = Constants.CanvasSize,
      wrap = (v: number) => (v < 0 ? v + s : v > s ? v - s : v),
   
    
    // all movement comes through here
    moveBody = (o: Body) =>
      <Body>{
        ...o,
        posx:wrap(o.posx-o.velocity)
      },

    handleCollisions = (s: State) => {
      
      const bodiesCollided = ([a, b]: [Body, Body]) => //checking if the bodies collided
          a.posy==b.posy? (a.posx>=b.posx && a.posx<=b.posx+b.width )? true:(a.posx+a.width>=b.posx && a.posx+a.width<=b.posx+b.width )?true:false:false,
         frogCollided = //return true if the frog collide with the car
          s.cars1.filter((r) => bodiesCollided([s.frog, r])).length>0||s.cars2.filter((r) => bodiesCollided([s.frog, r])).length>0||s.cars3.filter((r) => bodiesCollided([s.frog, r])).length>0||s.cars4.filter((r) => bodiesCollided([s.frog, r])).length>0,
          drown=([a,b]:[Body,Body])=> //checking if the body is in range of the object
          a.posy==b.posy? (a.posx>=b.posx && a.posx<b.posx+b.width &&a.posx+a.width>b.posx && a.posx+a.width<=b.posx+b.width )?false:true:false,
         frogDrown=//check if the frog is drown
          s.logs1.filter((r)=>drown([s.frog,r])).length==Constants.StartLogsCount1||s.logs2.filter((r)=>drown([s.frog,r])).length==Constants.StartLogsCount2||s.logs3.filter((r)=>drown([s.frog,r])).length==Constants.StartLogsCount3||s.logs4.filter((r)=>drown([s.frog,r])).length==Constants.StartLogsCount4,
          onlog=([a,b]:[Body,Body])=>!frogDrown&&a.posy==b.posy? //check if the on the log then the frog will get the velocity of the log
          {...s,frog:{...s.frog,velocity:b.velocity}}:{...s,frog:{...s.frog,velocity:0}},
          logs=[s.logs1[0]].concat(s.logs2[0],s.logs3[0],s.logs4[0]),
          currentlog=s.frog.posy==s.logs1[0].posy?0:s.frog.posy==s.logs2[0].posy?1:s.frog.posy==s.logs3[0].posy?2:s.frog.posy==s.logs4[0].posy?3:-1, // take the current row of the log
          frogOnLog1=logs.map(r=>onlog([s.frog,r]))[currentlog],//
          res=([a,b]:[Body,Body])=>bodiesCollided([a,b])?{...s,frog:createFrog()}:{...s},
          resforgoalline=([a,b]:[Body,Body])=>a.posy==b.posy?{...s,frog:createFrog()}:{...s},
          res_drown=([a,b]:[Body,Body])=>drown([a,b])?{...s,frog:createFrog()}:{...s},
          
          frogGoal=s.Goal.filter((r)=>bodiesCollided([s.frog,r])).length>0,//collide with goal
          frogonGoalLine=s.Goal.filter((r)=>s.frog.posy==r.posy).length>0,//is the frog enter the target line

          notonCroc=([a,b]:[Body,Body])=>// checking the frog on corcodile or not (not including the mouth)
          a.posy==b.posy? (a.posx>=b.posx && a.posx<b.posx+b.width-a.width &&a.posx+a.width>b.posx && a.posx+a.width<=b.posx+b.width-a.width )?false:true:false,
          res_diedOrdrown=([a,b]:[Body,Body])=>notonCroc([a,b])?{...s,frog:createFrog()}:{...s},
  
          frogDiedOrDrown=s.Croc.filter(r=>notonCroc([s.frog,r])).length==Constants.crocCount,//return true if the frog is collide with the area of the crocodile mouth
          oncroc=([a,b]:[Body,Body])=>!frogDiedOrDrown&&a.posy==b.posy?{...s,frog:{...s.frog,velocity:b.velocity}}:{...s,frog:{...s.frog,velocity:0}},//return body with velocity if the frog is on the back of the crocodile
          frogonCroc=s.Croc.map(r=>oncroc([s.frog,r]))[0],//adding velo to the frog

          frogres= // respwan frog
          s.Goal.map((r)=>resforgoalline([s.frog,r])).filter((r)=>s.frog!=r.frog)[0]
          ||s.cars1.concat(s.cars2,s.cars3,s.cars4).map((r)=>res([s.frog,r])).filter((r)=>s.frog!=r.frog)[0]
          ||s.logs1.concat(s.logs2,s.logs3,s.logs4).map((r)=>res_drown([s.frog,r])).filter((r)=>s.frog!=r.frog)[0]
          ||s.Croc.map(r=>res_diedOrdrown([s.frog,r])).filter((r)=>s.frog!=r.frog)[0]
          ||{...s}
          
          


          if(s.Goal.length==0){ // if all the goal is reached the game will over
            if(s.HighScore<s.Score){ // checking if we need to overwrite the high score
              return{
                ...s,
                gameover:true,
                HighScore:s.Score
              }
            }
            return<State>{
              ...s,
              gameover:true
            }
          }
          
          // 
          if(frogDrown||frogCollided||frogDiedOrDrown||frogonGoalLine){ //respawan the frog
            if(frogGoal){ // remove the goal which is reached and count the score.
              const v = s.Goal.filter((r)=>bodiesCollided([s.frog,r]))[0]
              const target=document.getElementById(v.id)!
              bg.removeChild(target)
              if(s.TOS<2000){
                return<State>{
                  ...s,
                Goal:s.Goal.filter((r)=>r!=v),
                frog:frogres.frog,
                isScore:true,
                Score:s.Score+200+2000-s.TOS,
                TOS:initialState.TOS
                }
              }
              return<State>{
                ...s,
                Goal:s.Goal.filter((r)=>r!=v),
                frog:frogres.frog,
                isScore:true,
                Score:s.Score+100,
                TOS:initialState.TOS
              }
            }
            return <State>{
              ...s,
              frog:frogres.frog,
              isScore:false
              
            };
          }
          if(currentlog>=0){
            return <State>{
          ...s,
          frog:frogOnLog1.frog
          }
        };
        return<State>{
          ...s,
          frog:frogonCroc.frog
        }
      },
      tick=(s:State,elapsed:number)=>{ // if nothing input is observed this function will run 

      return handleCollisions({
        ...s,
        
        frog:moveBody(s.frog),
        cars1:s.cars1.map(moveBody),
        cars2:s.cars2.map(moveBody),
        cars3:s.cars3.map(moveBody),
        cars4:s.cars4.map(moveBody),
        logs1:s.logs1.map(moveBody),
        logs2:s.logs2.map(moveBody),
        logs3:s.logs3.map(moveBody),
        logs4:s.logs4.map(moveBody),
        Croc:s.Croc.map(moveBody),
        time: elapsed,
        TOS:s.TOS+1,
        restart:false
      });}
    class Tick { constructor(public readonly elapsed:number) {} }
    class FB { constructor(public readonly movement:number) {} }
    class LR { constructor(public readonly movement:number) {} }
    class Reset {constructor(public readonly input:boolean){}}
    type Event = 'keydown' | 'keyup'
    type Key = 'KeyW' | 'KeyA' | 'KeyS'|'KeyD'|'KeyR'
    const observeKey = <T>(eventName:Event, k:Key, result:()=>T)=>
      fromEvent<KeyboardEvent>(document,eventName)
        .pipe(
          filter(({code})=>code === k),
          filter(({repeat})=>!repeat),
          map(result)),
      gameClock = interval(10)
       .pipe(map(elapsed=>new Tick(elapsed))),

    moveForward=observeKey('keydown','KeyW',()=>new FB(-24)),
    moveBackward=observeKey('keydown','KeyS',()=>new FB(24)),
    moveRight=observeKey('keydown','KeyD',()=>new LR(24)),
    moveLeft=observeKey('keydown','KeyA',()=>new LR(-24)),
    restart=observeKey('keydown','KeyR',()=>new Reset(true))
    //update the state
    const reduceState = (s:State, e:FB|LR|Tick|Reset)=>
    e instanceof FB ? {...s, 
      frog:{...s.frog,posy:(s.frog.posy+e.movement<600?s.frog.posy+e.movement>24?s.frog.posy+e.movement:s.frog.posy:s.frog.posy)},

    }: e instanceof LR?

    {...s,
      frog:{...s.frog,posx:(s.frog.posx+e.movement<600?s.frog.posx+e.movement>=0?s.frog.posx+e.movement:s.frog.posx:s.frog.posx)}
    }:e instanceof Reset?{
      ...initialState,
      HighScore:s.HighScore,
      restart:true}
    :tick(s,e.elapsed);
      
    const subscription=
    merge(gameClock,moveBackward,moveForward,moveLeft,moveRight,restart).pipe(scan(reduceState,initialState)).subscribe(updateView)

    function showKeys() {
      function showKey(k:Key) {
        const arrowKey = document.getElementById(k)!,
          o = (e:Event) => fromEvent<KeyboardEvent>(document,e).pipe(
            filter(({code})=>code === k))
        o('keydown').subscribe(_ => arrowKey.classList.add("highlight"))
        o('keyup').subscribe(_=>arrowKey.classList.remove("highlight"))
      }
      showKey('KeyW');
      showKey('KeyS');
      showKey('KeyA');
      showKey('KeyD');
      showKey('KeyR');
    }
    setTimeout(showKeys, 0)
}
 
// The following simply runs your main function on window load.  Make sure to leave it in place.
if (typeof window !== "undefined") {
  window.onload = () => {
    main();
  };
}
