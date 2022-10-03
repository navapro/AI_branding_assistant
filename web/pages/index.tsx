import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import CopyKitt from "../components/CopyKitt";
import styles from "../styles/Home.module.css";

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <meta
          name="description"
          content="Generated branding snippets and keywords for your product"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <CopyKitt />
    </div>
  );
};

export default Home;
