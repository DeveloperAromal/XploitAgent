"use client";

import { motion } from "framer-motion";

const roles = [
  "Developers",
  "AI Enthusiasts",
  "Security Researchers",
  "Digital Explorers",
  "Bug bounty Hunters",
];

export default function WhoThisIsFor() {
  return (
    <section className="flex items-center justify-center py-20 px-10 bg-black text-white">
      <div className="relative w-full rounded-3xl overflow-hidden max-w-">
        {/* Background */}
        <div className="absolute inset-0 ai-bg-1 z-0 rounded-3xl" />

        {/* Foreground */}
        <div className="relative z-10 p-12 h-[80vh] bg-black/50 rounded-3xl flex flex-col items-center justify-center">
          <div className="flex justify-between items-center gap-80">
            <div>
              <h2 className="text-6xl font-bold mb-4">Who This Is For</h2>
              <div className="bg-white text-neutral-900 w-20 py-2 rounded-xl text-center font-bold">
                <code># 1</code>
              </div>
            </div>
            <p className="text-lg max-w-md mx-auto text-right">
              This platform is designed for developers, AI enthusiasts, security
              researchers, and digital explorers who want to dive deeper into
              the world of intelligent systems, automation, and real-world
              applications of agentic AI.
            </p>
          </div>

          <div className="relative h-[700px] top-14 flex flex-col items-center justify-center">
            {roles.map((role, index) => (
              <motion.div
                key={role}
                initial={{ opacity: 0, y: 40 }}
                animate={{ opacity: 1, y: 0, marginBottom: 20 }}
                transition={{
                  delay: index * 0.5,
                  duration: 0.6,
                  type: "spring",
                  stiffness: 120,
                }}
                className="w-[600px] p-4 bg-white/10 border-2 border-white/20 backdrop-blur-2xl backdrop-saturate-150 text-black rounded-2xl shadow-[0_8px_24px_rgba(255,255,255,0.15)] text-center font-semibold -mt-8 "
                style={{
                  zIndex: roles.length + index,
                  width: 600 + index * 12,
                }}
              >
                <span className="w-3 h-3 rounded-full bg-green-500 absolute top-5 right-5 shadow-[0_0_12px_rgba(34,197,94,0.6)]"></span>

                <code className="text-white font-bold"> {role}</code>
              </motion.div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
