import Features from "./components/Features";
import Hero from "./components/Hero";
import Navbar from "./components/includes/Navbar";
import PainPoint from "./components/PainPoint";
import Solution from "./components/Solution";

export default function Home() {
  return (
    <main>
      <Navbar />
      <Hero />
      <PainPoint />
      <Solution />
      <Features />
    </main>
  );
}
