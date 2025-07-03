import { Fira_Code } from "next/font/google";

const firaCode = Fira_Code({
  variable: "--font-fira-code",
  subsets: ["latin"],
  weight: ["400", "700"],
});

export default function Loading() {
  return (
    <section
      className={`bg-black h-screen flex items-center justify-center ${firaCode.variable}`}
    >
      <div>
        <h1 className="text-4xl">Try hack me.......</h1>
      </div>
    </section>
  );
}
