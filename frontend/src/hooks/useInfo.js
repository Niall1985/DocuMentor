// import { useContext, useState } from "react";
// import toast from "react-hot-toast";
// import { InfoContext } from "../Context/InfoContext";

// const useInfo = () => {
//   const [loading, setLoading] = useState(false);
//   const [loading2, setLoading2] = useState(false);
//   const [multithreadedOutput, setMultithreadedOutput] = useState("");
//   const [sequentialOutput, setSequentialOutput] = useState("");
//   const { setTextThread, setNoThread } = useContext(InfoContext);

//   const getInfo = async (input) => {
//     setLoading(true);
//     setMultithreadedOutput(""); // Clear previous output
//     setSequentialOutput(""); // Clear previous output

//     try {
//       // API call to the multithreaded backend
//       console.log(input);
//       const multithreadedResponse = await fetch(
//         `http://localhost:9001/run-multithreaded?input=${encodeURIComponent(
//           input
//         )}`,
//         {
//           method: "GET",
//           headers: {
//             "Content-Type": "application/json",
//           },
//         }
//       );
//       if (!multithreadedResponse.ok) {
//         throw new Error(
//           "Multithreaded API call failed with status: " +
//             multithreadedResponse.status
//         );
//       }
//       const multithreadedData = await multithreadedResponse.json();
//       setMultithreadedOutput(multithreadedData.join("\n"));
//       console.log(multithreadedOutput);
//       setTextThread(multithreadedData.join("\n")); // Use the actual data

//       // API call to the sequential backend
//     } catch (error) {
//       toast.error("Internal Server Error: " + error.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   const getInfoWithoutThread = async () => {
//     setLoading2(true);
//     try {
//       const sequentialResponse = await fetch(
//         `http://localhost:9002/run-sequential?input=${encodeURIComponent(
//           input
//         )}`,
//         {
//           method: "GET",
//           headers: {
//             "Content-Type": "application/json",
//           },
//         }
//       );
//       if (!sequentialResponse.ok) {
//         throw new Error(
//           "Sequential API call failed with status: " + sequentialResponse.status
//         );
//       }
//       const sequentialData = await sequentialResponse.json();
//       setSequentialOutput(sequentialData.join("\n"));
//       setNoThread(sequentialData.join("\n")); // Use the actual data
//     } catch (error) {
//       toast.error("Internal Server Error: " + error.message);
//     } finally {
//       setLoading2(false);
//     }
//   };

//   return { loading, getInfo, getInfoWithoutThread, loading2 };
// };

// export default useInfo;

import { useContext, useState } from "react";
import toast from "react-hot-toast";
import { InfoContext } from "../Context/InfoContext";

const useInfo = () => {
  const [loading, setLoading] = useState(false);
  const [loading2, setLoading2] = useState(false);
  const [multithreadedOutput, setMultithreadedOutput] = useState("");
  const [sequentialOutput, setSequentialOutput] = useState("");
  const { setTextThread, setNoThread } = useContext(InfoContext);

  const getInfo = async (input) => {
    setLoading(true);
    setMultithreadedOutput(""); // Clear previous output
    setSequentialOutput(""); // Clear previous output

    try {
      // API call to the multithreaded backend
      const multithreadedResponse = await fetch(
        `http://localhost:9001/run-multithreaded?input=${encodeURIComponent(
          input
        )}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      if (!multithreadedResponse.ok) {
        throw new Error(
          "Multithreaded API call failed with status: " +
            multithreadedResponse.status
        );
      }
      const multithreadedData = await multithreadedResponse.json();
      setMultithreadedOutput(multithreadedData.join("\n"));
      console.log(multithreadedData)
      setTextThread(multithreadedData.join("\n")); // Use the actual data

      // Call to the sequential backend with input // Pass the input to the sequential function
    } catch (error) {
      toast.error("Internal Server Error: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  const getInfoWithoutThread = async (input) => {
    setLoading2(true);
    try {
      const sequentialResponse = await fetch(
        `http://localhost:9002/run-sequential?input=${encodeURIComponent(
          input
        )}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      if (!sequentialResponse.ok) {
        throw new Error(
          "Sequential API call failed with status: " + sequentialResponse.status
        );
      }
      const sequentialData = await sequentialResponse.json();
      setSequentialOutput(sequentialData.join("\n"));
      setNoThread(sequentialData.join("\n")); // Use the actual data
    } catch (error) {
      toast.error("Internal Server Error: " + error.message);
    } finally {
      setLoading2(false);
    }
  };

  return { loading, getInfo, getInfoWithoutThread, loading2 };
};

export default useInfo;
