const Response = ({ time,cpu,memory }) => {
  return (
    <>
    <div style={{fontSize:"18px"}}>{time}</div>
    <div style={{fontSize:"18px"}}>{cpu}</div>
    <div style={{fontSize:"18px"}}>{memory}</div>
    </>
  )
  
};

export default Response;
