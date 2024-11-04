// // import { useContext, useState } from "react";
// // import toast from "react-hot-toast";
// // import { InfoContext } from "../Context/InfoContext";

// // const useInfo = () => {
// //   const [loading, setLoading] = useState(false);
// //   const [multithreadedOutput, setMultithreadedOutput] = useState("");
// //   const [sequentialOutput, setSequentialOutput] = useState("");
// //   const { setTextThread, setNoThread } = useContext(InfoContext);

// //   const getInfo = async (input) => {
// //     setLoading(true);
// //     setMultithreadedOutput(""); 

// //     try {
// //       const multithreadedResponse = await fetch(
// //         `http://localhost:9001/run-multithreaded?input=${encodeURIComponent(input)}`,
// //         {
// //           method: "GET",
// //           headers: {
// //             "Content-Type": "text/plain",
// //           },
// //         }
// //       );

// //       if (!multithreadedResponse.ok) {
// //         throw new Error(
// //           "Multithreaded API call failed with status: " + multithreadedResponse.status
// //         );
// //       }

// //       const multithreadedData = await multithreadedResponse.text();
// //       const multithreadedStats = `\nResource Utilization Stats:\n${multithreadedData}`; 
// //       setMultithreadedOutput(multithreadedStats);
// //       setTextThread(multithreadedData);
// //       toast.success("Multithreaded data fetched successfully!");

// //     } catch (error) {
// //       toast.error("Internal Server Error: " + error.message);
// //     } finally {
// //       setLoading(false);
// //     }
// //   };

// //   const getInfoWithoutThread = async (input) => {
// //     setLoading(true);
// //     setSequentialOutput(""); 

// //     try {
// //       const sequentialResponse = await fetch(
// //         `http://localhost:9002/run-sequential?input=${encodeURIComponent(input)}`,
// //         {
// //           method: "GET",
// //           headers: {
// //             "Content-Type": "text/plain",
// //           },
// //         }
// //       );

// //       if (!sequentialResponse.ok) {
// //         throw new Error(
// //           "Sequential API call failed with status: " + sequentialResponse.status
// //         );
// //       }

// //       const sequentialData = await sequentialResponse.text();
// //       const sequentialStats = `\nResource Utilization Stats:\n${sequentialData}`; 
// //       setSequentialOutput(sequentialStats);
// //       setNoThread(sequentialData);
// //       toast.success("Sequential data fetched successfully!");

// //     } catch (error) {
// //       toast.error("Internal Server Error: " + error.message);
// //     } finally {
// //       setLoading(false);
// //     }
// //   };

// //   return { loading, getInfo, getInfoWithoutThread, multithreadedOutput, sequentialOutput };
// // };

// // export default useInfo;

// import { useContext, useState } from "react";
// import toast from "react-hot-toast";
// import { InfoContext } from "../Context/InfoContext";

// const useInfo = () => {
//   const [loading, setLoading] = useState(false);
//   const [multithreadedOutput, setMultithreadedOutput] = useState("");
//   const [sequentialOutput, setSequentialOutput] = useState("");
//   const { setTextThread, setNoThread } = useContext(InfoContext);
  
//   const [multithreadedStats, setMultithreadedStats] = useState("");
//   const [sequentialStats, setSequentialStats] = useState("");

//   const getInfo = async (input) => {
//     setLoading(true);
//     setMultithreadedOutput(""); 

//     try {
//       const multithreadedResponse = await fetch(
//         `http://localhost:9001/run-multithreaded?input=${encodeURIComponent(input)}`,
//         {
//           method: "GET",
//           headers: {
//             "Content-Type": "text/plain",
//           },
//         }
//       );

//       if (!multithreadedResponse.ok) {
//         throw new Error(
//           "Multithreaded API call failed with status: " + multithreadedResponse.status
//         );
//       }

//       const multithreadedData = await multithreadedResponse.text();
//       const [output, stats] = multithreadedData.split("\nTotal execution time: "); 
//       setMultithreadedOutput(output);
//       setMultithreadedStats(stats.trim());
//       setTextThread(multithreadedData);
//       toast.success("Multithreaded data fetched successfully!");

//     } catch (error) {
//       toast.error("Internal Server Error: " + error.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   const getInfoWithoutThread = async (input) => {
//     setLoading(true);
//     setSequentialOutput(""); 

//     try {
//       const sequentialResponse = await fetch(
//         `http://localhost:9002/run-sequential?input=${encodeURIComponent(input)}`,
//         {
//           method: "GET",
//           headers: {
//             "Content-Type": "text/plain",
//           },
//         }
//       );

//       if (!sequentialResponse.ok) {
//         throw new Error(
//           "Sequential API call failed with status: " + sequentialResponse.status
//         );
//       }

//       const sequentialData = await sequentialResponse.text();
//       const [output, stats] = sequentialData.split("\nTotal execution time: ");
//       setSequentialOutput(output);
//       setSequentialStats(stats.trim());
//       setNoThread(sequentialData);
//       toast.success("Sequential data fetched successfully!");

//     } catch (error) {
//       toast.error("Internal Server Error: " + error.message);
//     } finally {
//       setLoading(false);
//     }
//   };

//   return { loading, getInfo, getInfoWithoutThread, multithreadedOutput, sequentialOutput, multithreadedStats, sequentialStats };
// };

// export default useInfo;

import { useContext, useState } from "react";
import toast from "react-hot-toast";
import { InfoContext } from "../Context/InfoContext";

const useInfo = () => {
  const [loading, setLoading] = useState(false);
  const [multithreadedOutput, setMultithreadedOutput] = useState("");
  const [sequentialOutput, setSequentialOutput] = useState("");
  const { setTextThread, setNoThread } = useContext(InfoContext);

  const [multithreadedStats, setMultithreadedStats] = useState({
    executionTime: "",
    memoryUsage: "",
    cpuUsage: ""
  });
  
  const [sequentialStats, setSequentialStats] = useState({
    executionTime: "",
    memoryUsage: "",
    cpuUsage: ""
  });

  const parseStats = (data) => {
    const lines = data.split("\n");
    let output = "";
    let executionTime = "";
    let memoryUsage = "";
    let cpuUsage = "";

    lines.forEach(line => {
      if (line.startsWith("Total execution time:")) {
        executionTime = line.replace("Total execution time: ", "").trim();
      } else if (line.startsWith("Memory Usage:")) {
        memoryUsage = line.replace("Memory Usage: ", "").trim();
      } else if (line.startsWith("CPU Usage:")) {
        cpuUsage = line.replace("CPU Usage: ", "").trim();
      } else {
        output += line + "\n";
      }
    });

    return { output: output.trim(), executionTime, memoryUsage, cpuUsage };
  };

  const getInfo = async (input) => {
    setLoading(true);
    setMultithreadedOutput(""); 

    try {
      const multithreadedResponse = await fetch(
        `http://localhost:9001/run-multithreaded?input=${encodeURIComponent(input)}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "text/plain",
          },
        }
      );

      if (!multithreadedResponse.ok) {
        throw new Error(
          "Multithreaded API call failed with status: " + multithreadedResponse.status
        );
      }

      const multithreadedData = await multithreadedResponse.text();
      // const stats = parseStats(multithreadedData);
      // setMultithreadedOutput(stats.output);
      // setMultithreadedStats({
      //   executionTime: stats.executionTime,
      //   memoryUsage: stats.memoryUsage,
      //   cpuUsage: stats.cpuUsage
      // });
      // console.log()
      setTextThread(multithreadedData);
      toast.success("Multithreaded data fetched successfully!");

    } catch (error) {
      toast.error("Internal Server Error: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  const getInfoWithoutThread = async (input) => {
    setLoading(true);
    setSequentialOutput(""); 

    try {
      const sequentialResponse = await fetch(
        `http://localhost:9002/run-sequential?input=${encodeURIComponent(input)}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "text/plain",
          },
        }
      );

      if (!sequentialResponse.ok) {
        throw new Error(
          "Sequential API call failed with status: " + sequentialResponse.status
        );
      }

      const sequentialData = await sequentialResponse.text();
      const stats = parseStats(sequentialData);
      setSequentialOutput(stats.output);
      setSequentialStats({
        executionTime: stats.executionTime,
        memoryUsage: stats.memoryUsage,
        cpuUsage: stats.cpuUsage
      });
      setNoThread(sequentialData);
      toast.success("Sequential data fetched successfully!");

    } catch (error) {
      toast.error("Internal Server Error: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return { 
    loading, 
    getInfo, 
    getInfoWithoutThread, 
    multithreadedOutput, 
    sequentialOutput, 
    multithreadedStats, 
    sequentialStats 
  };
};

export default useInfo;
