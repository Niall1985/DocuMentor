import { useContext, useEffect, useState } from "react";
import { InfoContext } from "../Context/InfoContext";
import { FaArrowRight } from "react-icons/fa6";
import { IoGlobeSharp } from "react-icons/io5";
import Content from "./Content";

const WithThread = () => {
  const { textThread } = useContext(InfoContext);
  const [answer, setAnswer] = useState([]);
  const [loading, setLoading] = useState(true); // Initialize loading state
  // console.log(textThread.split(" "))
  useEffect(() => {
    if (textThread) {
      // Match all occurrences of quoted strings
      const quotedContents = textThread.match(/"(.*?)"/g);
      
      // Extract only the relevant quotes, removing the quotes themselves
      const relevantQuotes = quotedContents
        ? quotedContents
            .map(match => match.replace(/"/g, '')) // Remove the quotes
            .filter(content => content.includes("No relevant content found")) // Filter for relevant content
        : []; // Handle case when no matches are found

      setAnswer(relevantQuotes); // Update the state with relevant quotes
      setLoading(false); // Set loading to false after processing
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
      {loading ? (
        <>
          <div className="spinner-border spin" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <div style={{ marginLeft: "265px", fontSize: "20px" }}>
            Fetching contents...
          </div>
        </>
      ) : (
        <div style={{ margin: "10px 20px 0 20px" }}>
          <FaArrowRight />{answer.length === 0 ? (
            <div></div>
          ) : (
            answer.map((ans, index) => (
              <Content key={index} quote={ans} /> // Render each quote
            ))
          )}
        </div>
      )}
    </div>
  );
};

export default WithThread;
