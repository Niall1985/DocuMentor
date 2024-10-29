import { Children, createContext, useState } from "react";

export const InfoContext = createContext({});

export const InfoContextProvider = ({ children }) => {
  const [infoMode, setInfoMode] = useState(false);
  const [text, setText] = useState("");
  const [question, setQuestion] = useState("");
  const [textThread, setTextThread] = useState("");
  const [textNoThread, setNoThread] = useState("");
  return (
    <InfoContext.Provider
      value={{
        infoMode,
        setInfoMode,
        text,
        setText,
        question,
        setQuestion,
        textThread,
        setTextThread,
        textNoThread,
        setNoThread,
      }}
    >
      {children}
    </InfoContext.Provider>
  );
};
