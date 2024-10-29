import { useState } from "react";
import UserEntry from "./components/userEntry";
import WithoutThread from "./components/WithoutThread";
import WithThread from "./components/WithThread";

const App = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <UserEntry />
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <WithoutThread />
        <WithThread />
      </div>
    </div>
  );
};

export default App;
