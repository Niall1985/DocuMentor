import UserEntry from "./components/userEntry";
import WithoutThread from "./components/WithoutThread";
import WithThread from "./components/WithThread";
import { Toaster } from "react-hot-toast";
import "bootstrap/dist/css/bootstrap.css";
import ResponseContainer from "./components/ResponeContainer";

const App = () => {
  return (
    <>
      <div
        style={{
          margin: "20px",
          backgroundColor: "rgb(205, 226, 226)",
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
        <ResponseContainer />
      </div>
      <Toaster />
    </>
  );
};

export default App;
