import { useContext, useEffect, useState } from "react";
import useInfo from "../hooks/useInfo";
import { InfoContext } from "../Context/InfoContext";
import Response from "./Response";

const ResponseContainer = () => {
  const [time1, setTime1] = useState("");
  const [time2, setTime2] = useState("");
  const { infoMode } = useContext(InfoContext);
  const { loading, loading2, textThread, textNoThread } = useContext(InfoContext);
    // console.log(textThread)
  const handleResponseTime = (text) => {
    const regex = /Total execution time: (\d+m)?\d*\.?\d*s/;
    const match = text.match(regex);
    return match ? match[0] : "Not found!!!"; // Extract the time or return "Not found!!!"
  };

  const convertToSeconds = (time) => {
    const regex = /(\d+)m(\d+\.?\d*)s/; // Regex to match minutes and seconds
    const match = time.match(regex);
  
    if (match) {
      const minutes = parseFloat(match[1]);
      const seconds = parseFloat(match[2]);
      return minutes * 60 + seconds; // Convert minutes to seconds and add seconds
    }
    
    return 0; // Return 0 if no match
  };


  useEffect(() => {
    // console.log("Helooooooooooooooooooooooooooooo")
    // const {textThread}=useInfo()
    if (textThread) {
        console.log(textThread)
    // console.log("Working...")
      const extractedTime = handleResponseTime(textThread);
      if(extractedTime=="Not found!!!"){
        setTime1("0");
      }else{
          setTime1(extractedTime);
      }
    //   const totalSeconds = convertToSeconds(extractedTime);
    }else{
        setTime1("")
    }
  }, [textThread]);

  useEffect(() => {
    if (textNoThread) {
        console.log(textNoThread)
      const extractedTime = handleResponseTime(textNoThread);
    //   const totalSeconds = convertToSeconds(extractedTime);
      if(extractedTime=="Not found!!!"){
        setTime2("0");
      }else{
          setTime2(extractedTime);
      }
    //   setTime2(totalSeconds);
    }else{
        setTime2("")
    }
  }, [textNoThread]);

  return (
    <div style={{display:"flex",justifyContent:"space-between",paddingLeft:"30px",paddingTop:"10px",paddingRight:"440px"}}>
      {time1 && infoMode && (
        <div
        
        >
          <Response time={time2} />
        </div>
      )}
      {time2 && infoMode && (
        <div
          
        >
          <Response time={time1} />
        </div>
      )}
    </div>
  );
};

export default ResponseContainer;
