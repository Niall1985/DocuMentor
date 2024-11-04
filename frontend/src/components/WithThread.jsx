// import { useContext, useEffect, useState } from "react";
// import { InfoContext } from "../Context/InfoContext";
// import { FaArrowRight } from "react-icons/fa6";
// import { IoGlobeSharp } from "react-icons/io5";
// import Content from "./Content";
// import useInfo from "../hooks/useInfo";

// const WithThread = () => {
//   const { textThread } = useContext(InfoContext);
//   console.log(textThread)
//   const [answer, setAnswer] = useState([]);
//   const [loading3, setLoading3] = useState(true); // Initialize loading state
//   // console.log(textThread.split(" "))

//   useEffect(() => {
//     if (textThread) {
//       // const {loading}=useInfo()
//       // setLoading3(loading)
//       // setLoading3(loading)
//       // Match all occurrences of quoted strings
//       console.log("I am inside the function")
//       const quotedContents = textThread.match(/"(.*?)"/g);

//       // Extract only the relevant quotes, removing the quotes themselves
//       const relevantQuotes = quotedContents
//         ? quotedContents
//             .map(match => match.replace(/"/g, '')) // Remove the quotes
//             .filter(content => content.includes("No relevant content found")) // Filter for relevant content
//         : []; // Handle case when no matches are found

//       setAnswer(relevantQuotes); // Update the state with relevant quotes
//       setLoading3(false); // Set loading to false after processing
//     }
//   }, [textThread]); // Dependency array ensures effect runs when textThread changes

//   const { infoMode, question } = useContext(InfoContext);

//   return (
//     <div className={`content ${infoMode ? "" : "hide"}`}>
//       <h1
//         style={{
//           margin: "10px 20px 0 20px",
//           textAlign: "center",
//           marginBottom: "40px",
//         }}
//       >
//         With Threads
//       </h1>
//       <div style={{ marginLeft: "10px" }}>
//         <IoGlobeSharp /> {question} <IoGlobeSharp />
//       </div>
//       {loading3 ? (
//         <>
//           <div className="spinner-border spin" role="status">
//             <span className="visually-hidden">Loading...</span>
//           </div>
//           <div style={{ marginLeft: "265px", fontSize: "20px" }}>
//             Fetching contents...
//           </div>
//         </>
//       ) : (
//         <div style={{ margin: "10px 20px 0 20px" }}>
//           <FaArrowRight />{answer.length === 0 ? (
//             <div></div>
//           ) : (
//             answer.map((ans, index) => (
//               <Content key={index} quote={ans} /> // Render each quote
//             ))
//           )}
//         </div>
//       )}
//     </div>
//   );
// };

// export default WithThread;

import { useContext, useEffect, useState } from "react";
import { InfoContext } from "../Context/InfoContext";
import { FaArrowRight } from "react-icons/fa6";
import { IoGlobeSharp } from "react-icons/io5";
import Content from "./Content";

const WithThread = () => {
  const { textThread } = useContext(InfoContext);
  const [answer, setAnswer] = useState([]);
  const [loading3, setLoading3] = useState(true); // Initialize loading state
  // const [loading,setLoading]=useState(true)

  useEffect(() => {
    setLoading3(true);
    // setLoading(true)
    // console.log(loading3,loading);
    if (textThread) {
      // console.log(loading3,loading);

      // Match all occurrences of quoted strings
      // const quotedContents = textThread.match(/"(.*?)"/g);

      // // Extract only the relevant quotes, removing the quotes themselves
      // const relevantQuotes = quotedContents
      //   ? quotedContents
      //       .map(match => match.replace(/"/g, '')) // Remove the quotes
      //       .filter(content => content.includes("No relevant content found")) // Filter for relevant content
      //   : []; // Handle case when no matches are found

      const regex = /Chunk from #\d+\.pdf:\s*([\s\S]*?)(?=\n{2}|\Z)/g;

      const array = [];
      let match;

      while ((match = regex.exec(textThread)) !== null) {
        // Trim whitespace and push the match to the array
        array.push(match[1].trim());
      }

      let cleanedArray = array.map((item) =>
        item.replace(/[\r\n]+/g, " ").trim()
      );
      // Display the resulting array
      console.log(cleanedArray);

      const count = cleanedArray.filter((item) =>
        item.includes("No relevant content found")
      ).length;
      // console.log(count)
      if (count == 6) {
        cleanedArray = ["No relevant Data found"];
      } else {
        cleanedArray = cleanedArray.filter(
          (item) => !item.startsWith("No relevant content")
        );
      }
      setAnswer(cleanedArray); // Update the state with relevant quotes
      console.log("heloooo");
      setLoading3(false); // Set loading to false after processing
      // setLoading(false); // Set loading to false after processing
      // console.log(loading3,loading)
    } else {
      // Handle case where textThread is empty or undefined
      setAnswer([]);
      // setLoading3(false);
    }
  }, [textThread]); // Dependency array ensures effect runs when textThread changes

  const { infoMode, question } = useContext(InfoContext);

  return (
    <div className={`content ${infoMode ? "" : "hide"}`}>
      <h1
        style={{
          margin: "10px 20px 0 20px",
          textAlign: "center",
          marginBottom: "40px",
        }}
      >
        With Threads
      </h1>
      <div style={{ marginLeft: "10px" }}>
        <IoGlobeSharp /> {question} <IoGlobeSharp />
      </div>
      {loading3 ? (
        <>
          <div className="spinner-border spin" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <div style={{ marginLeft: "255px", fontSize: "20px" }}>
            Fetching contents...
          </div>
        </>
      ) : (
        <div style={{ margin: "10px 20px 0 20px" }}>
          <FaArrowRight />
          {answer.length === 0 ? (
            <div></div> 
          ) : (
            answer.map((ans, index) => (
              <Content key={index} quote={ans} />
            ))
          )}
        </div>
      )}
    </div>
  );
};

export default WithThread;
