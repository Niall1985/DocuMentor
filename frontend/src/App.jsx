import { useState } from "react";
import UserEntry from "./components/userEntry";
import WithoutThread from "./components/WithoutThread";
import WithThread from "./components/WithThread";
import { Toaster } from "react-hot-toast";
import "bootstrap/dist/css/bootstrap.css";

const App = () => {
  const [count, setCount] = useState(0);

  return (
    <>
      <div>
        <UserEntry />
        <div style={{ display: "flex", justifyContent: "space-between" }}>
          <WithoutThread />
          <WithThread />
        </div>
      </div>
      <Toaster />
    </>
  );
};

export default App;
