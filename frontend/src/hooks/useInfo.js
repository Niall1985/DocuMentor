import { useState } from "react";
import toast from "react-hot-toast";

const useInfo = () => {
  const [loading, setLoading] = useState(false);
  const getInfo = async () => {
    setLoading(true);
    try {
      // add api call here
    } catch (error) {
      toast.error("Internal Server Error...");
    } finally {
      setLoading(false);
    }
  };
  return { loading, getInfo };
};
