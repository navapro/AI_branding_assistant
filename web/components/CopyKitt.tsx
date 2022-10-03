import React from "react";
import { useState } from "react";

const CopyAi: React.FC = () => {
  const [propmt, setPrompt] = useState("");
  const onSubmit = () => {};
  return (
    <>
      <h1>CopyAI</h1>
      <p>
        Tell me what your brand is about and I will generate copy and keywords
        for you.
      </p>
      <input
        type="text"
        placeholder="coffee"
        onChange={(e) => {
          setPrompt(e.currentTarget.value);
        }}
        value={propmt}
      ></input>
      <button onClick={onSubmit}>Submit</button>
    </>
  );
};

export default CopyAi;
