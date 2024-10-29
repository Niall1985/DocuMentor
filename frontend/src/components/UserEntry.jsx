import { useState } from "react";
import { FaArrowRight } from "react-icons/fa6";
const UserEntry = () => {
  const [query, setQuery] = useState("");
  const handleDivClick = (e) => {
    setQuery(e.target.innerText);
  };

  return (
    <div
      style={{
        marginTop: "40px",
        width: "100%",
        height: "240px",
      }}
    >
      <h1 style={{ fontSize: "42px", textAlign: "center" }}>DocuMentor</h1>
      <form style={{ position: "relative" }}>
        <input
          placeholder="Enter the query..."
          style={{
            height: "25px",
            width: "300px",
            marginLeft: "600px",
          }}
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        ></input>
        <button
          style={{
            height: "30px",
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