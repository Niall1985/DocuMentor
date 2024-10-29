import { useContext, useState } from "react";
import { InfoContext } from "../Context/InfoContext";
import { FaArrowRight } from "react-icons/fa6";
import { IoGlobeSharp } from "react-icons/io5";

const WithThread = () => {
  const [loading, setLoading] = useState(false);
  const { infoMode, question } = useContext(InfoContext);
  return (
    <div className={`content ${infoMode ? "" : "hide"}`}>
      <h1
        style={{
          margin: "10px 20px 0 20px",
          textAlign: "center",
          marginBottom: "40px",
        }}
      >
        With Threads
      </h1>
      <div style={{ marginLeft: "10px" }}>
        <IoGlobeSharp /> {question} <IoGlobeSharp />
      </div>
      {loading ? (
        <>
          <div class="spinner-border spin" role="status">
            <span class="visually-hidden">Loading...</span>
          </div>
          <div style={{ marginLeft: "265px", fontSize: "20px" }}>
            Fetching contents...
          </div>
        </>
      ) : (
        <div style={{ margin: "10px 20px 0 20px" }}>
          <FaArrowRight /> Lorem ipsum dolor sit amet consectetur adipisicing
          elit. Deleniti distinctio reprehenderit atque harum itaque voluptate
          natus. Dolore cum aspernatur eveniet architecto? Laborum non veritatis
          quo magni eveniet consequuntur sunt id. Temporibus fugiat corporis
          culpa, commodi optio expedita libero qui ullam mollitia reiciendis,
          dolor harum adipisci dolorum blanditiis praesentium alias ducimus nam
          ut odio esse quasi ipsa similique explicabo? Eaque, voluptatibus!
          Perferendis cum vel doloremque ad doloribus ratione similique
          distinctio dolor pariatur eum voluptate voluptas optio tenetur autem
          deserunt, nesciunt odio quod architecto debitis recusandae aspernatur.
          Quaerat dignissimos minima sint illum. Quia, exercitationem officiis!
          Est nam nisi iusto voluptates, neque praesentium perferendis
          assumenda. Doloremque facilis facere numquam delectus recusandae,
          corrupti placeat quidem, quas quasi earum voluptatibus sapiente nam
          error atque reiciendis! Eaque quas voluptatibus, perferendis, impedit
          a et aliquid dolorum fugiat numquam expedita reprehenderit labore,
          quae provident vitae repellat reiciendis optio sunt quia dolores?
          Maiores quaerat alias ad eveniet! Ducimus, error. Perferendis ab
          doloribus iusto in a eaque laborum, iure accusamus, porro ut magnam
          tenetur necessitatibus quasi beatae quidem neque. Optio repudiandae
          ipsa magni inventore a adipisci sunt labore, dolorem vel? Dignissimos
          veniam repellendus laudantium earum beatae laboriosam expedita fuga,
          rem, fugiat eaque voluptate, eligendi cum ex minus voluptas totam
          aspernatur doloribus sed? Dolor, laborum. Fuga nulla itaque ex quos
          quasi? Doloremque amet vero autem necessitatibus sint accusamus
          temporibus distinctio voluptatibus porro consequuntur eius dignissimos
          natus aliquid commodi in saepe, ipsum officiis dolorem, illo
          repellendus facere sapiente, quam recusandae! Vel, tempora. Omnis
          expedita saepe earum consequuntur aliquid ipsa a recusandae nisi
          tempora officiis laboriosam doloremque distinctio autem id nam
          voluptatibus maxime ipsam corporis, odio exercitationem neque
          architecto illo mollitia. Dolor, nobis! Quasi eaque at, omnis eos
          optio dicta maiores iste placeat, ipsum quo nulla laboriosam id porro,
          vitae repellat necessitatibus. Impedit ipsam quis perspiciatis error
          tempora fuga, ea explicabo rerum libero?
        </div>
      )}
    </div>
  );
};

export default WithThread;
