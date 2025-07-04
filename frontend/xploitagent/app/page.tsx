import Features from "./components/Features";
import Hero from "./components/Hero";
import Footer from "./components/includes/Footer";
import Navbar from "./components/includes/Navbar";
import LatestNews from "./components/LatestNews";
import PainPoint from "./components/PainPoint";
import Solution from "./components/Solution";
import Threat from "./components/Threat";
import WhoThisIsFor from "./components/WhoThisIsFor";

export default function Home() {
  return (
    <main className="">
      <Navbar />
      <Hero />
      <LatestNews />
      <Threat />
      <WhoThisIsFor />
      {/* <PainPoint /> */}
      {/* <Solution /> */}
      {/* <Features /> */}
      <Footer />
    </main>
  );
}
