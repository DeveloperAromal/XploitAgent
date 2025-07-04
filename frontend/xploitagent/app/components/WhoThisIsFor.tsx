"use client";

import {
  Code,
  Rocket,
  ShieldCheck,
  Building2,
  BrainCircuit,
} from "lucide-react";

import { useState } from "react";

export default function WhoThisIsFor() {
  const buyers = [
    {
      tab: "Developers",
      title: "Build fast, stay secure.",
      content:
        "As a developer, you ship fast — but security gets left behind. Our AI scans your code and endpoints for vulnerabilities so you can focus on building without fear of leaks, hacks, or data exposure.",
      icon: Code,
    },
    {
      tab: "Startup Founders",
      title: "Security without the overhead.",
      content:
        "Hiring a security team is expensive. Our agentic AI gives you full-scale vulnerability reports, threat analysis, and fix suggestions — all automated, so you don’t burn investor cash on manual audits.",
      icon: Rocket,
    },
    {
      tab: "Agencies",
      title: "Secure your clients, build your rep.",
      content:
        "Clients trust you to build secure systems. Our tool runs deep scans on every project before handoff — helping you avoid post-launch breaches, and making your agency look even more pro.",
      icon: ShieldCheck,
    },
    {
      tab: "Enterprises",
      title: "Stay compliant and bulletproof.",
      content:
        "Compliance rules are getting stricter. Whether it's GDPR, HIPAA, or SOC 2 — our AI detects risky areas in your systems and helps keep you audit-ready, saving thousands in penalties.",
      icon: Building2,
    },
    {
      tab: "AI/ML Engineers",
      title: "Don't let your model get wrecked.",
      content:
        "AI apps are vulnerable too — prompt injection, backend logic flaws, or token exposure. Our AI understands how your AI works — and protects it from nasty edge-case exploits.",
      icon: BrainCircuit,
    },
  ];

  const [activeTab, setActiveTab] = useState(buyers[0].tab);

  const activeBuyer = buyers.find((b) => b.tab === activeTab);

  return (
    <section className="mt-20  px-10 py-30 w-full h-screen rounded-t-2xl">
      <div className="top mb-25 flex flex-col items-center justify-center">
        <span className="font-bold text-[var(--primary-text)] mb-8">
          Hey brother FOCUS
        </span>
        <h3 className="font-semibold text-6xl">Who Should Buy This</h3>
      </div>
      <div className="bottom">
        <div className="tabs flex items-center justify-center space-x-10 flex-wrap">
          {buyers.map(({ tab, icon: Icon }) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`tab flex items-center space-x-2 py-2 px-4 transition-all duration-200 border-b-2 ${
                activeTab === tab
                  ? "border-[var(--primary)] text-white"
                  : "border-transparent text-gray-400 hover:text-white"
              }`}
            >
              <Icon className="w-5 h-5" />
              <span className="text-md font-medium">{tab}</span>
            </button>
          ))}
        </div>

        {/* Details */}
        {activeBuyer && (
          <div className="mt-16 max-w-4xl mx-auto text-center">
            <h4 className="text-3xl font-semibold mb-4">{activeBuyer.title}</h4>
            <p className="text-lg text-gray-300">{activeBuyer.content}</p>
          </div>
        )}
      </div>
    </section>
  );
}
