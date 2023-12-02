"use client";
import styles from "@/styles/page.module.css";
import Uploads from "@/components/Uploads";
import React, { useState } from "react";
import usePYModels from "@/hook/usePYModels";
import Image from "next/image";

export default function Home() {
  const { predictpetclassifyhub } = usePYModels();
  const [images, setImages] = useState([]);
  const [prediction, setPrediction] = useState([]);
  const submit = async () => {
    const response = await predictpetclassifyhub(images);
    setPrediction(response);
  };

  return (
    <div className={styles.container}>
      <Uploads images={images} setImages={setImages} />
      <div className={styles.submit}>
        <button onClick={submit}>Recognize</button>
      </div>
      <div className={styles.predictions}>
        {prediction.map((item) => (
          <div key={item.id} className={styles.prediction}>
            <Image src={item.url} alt="img" width={250} height={250} />
            <div>
              <h5>Name: {item.name}</h5>
              <p>Prediction: {item.prediction}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
