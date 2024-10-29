import { useContext, useState } from "react";
import UserEntry from "./components/userEntry";
import WithoutThread from "./components/WithoutThread";
import WithThread from "./components/WithThread";
import { Toaster } from "react-hot-toast";
import "bootstrap/dist/css/bootstrap.css";
import Response from "./components/Response";
import { InfoContext } from "./Context/InfoContext";
import useInfo from "./hooks/useInfo";

const App = () => {
  const [count, setCount] = useState(0);
  const { infoMode } = useContext(InfoContext);
  const { loading } = useInfo();
  // const [loading, setLoading] = useState(true);

  const time = "20ms";
  return (
    <>
      <div
        style={{
          margin: "20px",
          backgroundColor: "#FFDEAD",
          borderRadius: "20px",
          paddingTop: "6px",
          paddingBottom: "10px",
        }}
      >
        <UserEntry />
        <div style={{ display: "flex", justifyContent: "space-between" }}>
          <WithoutThread />
          <WithThread />
        </div>
        {loading && infoMode ? (
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              paddingLeft: "20px",
              paddingRight: "580px",
              paddingTop: "5px",
            }}
          >
            <Response time={time} />
            <Response time={time} />
          </div>
        ) : (
          <></>
        )}
      </div>
      <Toaster />
    </>
  );
};

export default App;
