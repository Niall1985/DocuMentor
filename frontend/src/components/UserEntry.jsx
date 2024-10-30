import { useContext, useState } from "react";
import { FaArrowRight } from "react-icons/fa6";
import { InfoContext } from "../Context/InfoContext";
import useInfo from "../hooks/useInfo";
import toast from "react-hot-toast";
const UserEntry = () => {
  const [query, setQuery] = useState("");
  const { setInfoMode, setQuestion } = useContext(InfoContext);
  const { getInfo } = useInfo();
  const handleDivClick = (e) => {
    setQuery(e.target.innerText);
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    if (!query) {
      toast("Enter the Query??", {
        icon: "👇",
        style: {
          borderRadius: "10px",
          background: "#333",
          color: "#fff",
        },
      });
      return;
    }
    setQuestion(query);
    getInfo(query);
    setQuery("");
    setInfoMode(true);
  };

  return (
    <div
      style={{
        marginTop: "40px",
        width: "100%",
        height: "240px",
      }}
    >
      <h1
        style={{ fontSize: "42px", textAlign: "center", marginBottom: "35px" }}
      >
        DocuMentor
      </h1>
      <form style={{ position: "relative" }} onSubmit={handleFormSubmit}>
        <input
          placeholder="Enter the query..."
          style={{
            height: "45px",
            width: "300px",
            marginLeft: "600px",
          }}
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        ></input>
        <button
          style={{
            height: "46px",
            width: "50px",
            zIndex: "1",
            position: "absolute",
            right: "39%",
          }}
        >
          <div style={{ marginTop: "3px" }}>
            <FaArrowRight />
          </div>
        </button>
      </form>
      <div
        style={{ display: "flex", justifyContent: "center", marginTop: "40px" }}
      >
        <div className="suggestions" onClick={handleDivClick}>
          Latest technology used in agriculture
        </div>
        <div className="suggestions" onClick={handleDivClick}>
          Latest technology used in agriculture2
        </div>
        <div className="suggestions" onClick={handleDivClick}>
          Latest technology used in agriculture3
        </div>
        <div className="suggestions" onClick={handleDivClick}>
          Latest technology used in agriculture4
        </div>
      </div>
    </div>
  );
};

export default UserEntry;
