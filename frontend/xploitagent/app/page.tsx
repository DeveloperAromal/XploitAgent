import Features from "./components/Features";
import Hero from "./components/Hero";
import Navbar from "./components/includes/Navbar";
import LatestNews from "./components/LatestNews";
import PainPoint from "./components/PainPoint";
import Solution from "./components/Solution";
import Threat from "./components/Threat";

export default function Home() {
  return (
    <main>
      <Navbar />
      <Hero />
      <LatestNews />
      <Threat />
      <PainPoint />
      <Solution />
      <Features />
    </main>
  );
}
