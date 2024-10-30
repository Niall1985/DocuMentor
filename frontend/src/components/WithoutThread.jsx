import { useContext, useEffect, useState } from "react";
import { InfoContext } from "../Context/InfoContext";
import { FaArrowRight } from "react-icons/fa6";
import useInfo from "../hooks/useInfo";
import { IoGlobeSharp } from "react-icons/io5";
import Content from "./Content";

const WithoutThread = () => {
  // const [loading, setLoading] = useState(true);
  // let loading2=true
  // const { textNoThread } = useContext(InfoContext);
  // const { textThread } = useContext(InfoContext);
  const { textNoThread } = useContext(InfoContext);
  const [answer, setAnswer] = useState([]);
  const [loading2, setLoading2] = useState(true); // Initialize loading state

  useEffect(() => {
    if (textNoThread) {
      // Match all occurrences of quoted strings
      const quotedContents = textNoThread.match(/"(.*?)"/g);
      
      // Extract only the relevant quotes, removing the quotes themselves
      const relevantQuotes = quotedContents
        ? quotedContents
            .map(match => match.replace(/"/g, '')) // Remove the quotes
            .filter(content => content.includes("No relevant content found")) // Filter for relevant content
        : []; // Handle case when no matches are found

      setAnswer(relevantQuotes); // Update the state with relevant quotes
      setLoading2(false); // Set loading to false after processing
    }
  }, [textNoThread]); // Dependency array ensures effect runs when textThread changes

  const { infoMode, question } = useContext(InfoContext)
  return (
    <>
      <div className={`content ${infoMode ? "" : "hide"}`}>
        <h1
          style={{
            margin: "10px 20px 0 20px",
            textAlign: "center",
            marginBottom: "40px",
          }}
        >
          Without Threads
        </h1>
        <div style={{ marginLeft: "10px" }}>
          <IoGlobeSharp /> {question} <IoGlobeSharp />
        </div>
        {loading2 ? (
          <>
            <div class="spinner-border spin" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
            <div style={{ marginLeft: "265px", fontSize: "20px" }}>
              Fetching contents...
            </div>
          </>
        ) : (
          <div style={{ margin: "10px 20px 0 20px" }}>
            <FaArrowRight /> {answer.length === 0 ? (
            <div></div>
          ) : (
            answer.map((ans, index) => (
              <Content key={index} quote={ans} /> // Render each quote
            ))
          )}
          </div>
        )}
      </div>
    </>
  );
};

export default WithoutThread;
