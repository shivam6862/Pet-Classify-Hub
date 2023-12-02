import React from "react";
import classes from "@/styles/header.module.css";
import Image from "next/image";

const Header = () => {
  return (
    <div className={classes.container}>
      <div className={classes.box}>
        <Image src={"/logo.png"} width={40} height={40} alt="logo" />
        Pet Classify Hub
      </div>
    </div>
  );
};

export default Header;
