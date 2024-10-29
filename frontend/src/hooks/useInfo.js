import { useContext, useState } from "react";
import toast from "react-hot-toast";
import { InfoContext } from "../Context/InfoContext";

const useInfo = () => {
  const [loading, setLoading] = useState(false);
  const [multithreadedOutput, setMultithreadedOutput] = useState("");
  const [sequentialOutput, setSequentialOutput] = useState("");
  const { setTextThread, setNoThread } = useContext(InfoContext);

  const getInfo = async (input) => {
    setLoading(true);
    try {
      // API call to the multithreaded backend
      const multithreadedResponse = await fetch(
        `http://localhost:8081/run-multithreaded?input=${encodeURIComponent(
          input
        )}`
      );
      if (!multithreadedResponse.ok) {
        throw new Error("Multithreaded API call failed");
      }
      const multithreadedData = await multithreadedResponse.json();
      setMultithreadedOutput(multithreadedData.join("\n"));
      setTextThread(multithreadedOutput);
      // API call to the sequential backend
      const sequentialResponse = await fetch(
        `http://localhost:8082/run-sequential?input=${encodeURIComponent(
          input
        )}`
      );
      if (!sequentialResponse.ok) {
        throw new Error("Sequential API call failed");
      }
      const sequentialData = await sequentialResponse.json();
      setSequentialOutput(sequentialData.join("\n"));
      setNoThread(sequentialOutput);
    } catch (error) {
      toast.error("Internal Server Error: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return { loading, getInfo, multithreadedOutput, sequentialOutput };
};

export default useInfo;
