import React from "react";
import { Shield, Brain, BarChart2 } from "lucide-react";

export default function WhyChooseEyeShield() {
  return (
    <section className="bg-[#add8ff] text-[#001f33] py-16 px-8">
      <div className="max-w-6xl mx-auto text-center">
        <h2 className="text-4xl font-bold mb-4">Why Choose EYESHIELD?</h2>
        <p className="text-[#00334d] mb-12">
          EYESHIELD is an advanced, AI-driven cybersecurity solution designed to offer unparalleled protection
          against modern cyber threats. Our system provides real-time, autonomous defense,
          ensuring your digital assets are safeguarded 24/7 with minimal intervention.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="bg-[#cce5ff] rounded-xl p-6 hover:shadow-lg transition">
            <div className="mb-4 flex justify-center">
              <div className="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow">
                <Brain className="w-8 h-8 text-[#004080]" />
              </div>
            </div>
            <h3 className="text-xl font-semibold mb-2">AI-Powered Threat Detection</h3>
            <p className="text-[#00334d] mb-10">
              Leverage advanced AI to identify and neutralize cyber threats in real-time,keeping your system secure around the clock.
            </p>
            <a href="#" className="text-[#004080] hover:underline">Learn More →</a>
          </div>

          <div className="bg-[#cce5ff] rounded-xl p-6 hover:shadow-lg transition">
            <div className="mb-4 flex justify-center">
              <div className="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow">
                <Shield className="w-8 h-8 text-[#004080]" />
              </div>
            </div>
            <h3 className="text-xl font-semibold mb-2">Seamless, Invisible Protection</h3>
            <p className="text-[#00334d] mb-12">
              EYESHIELD integrates quietly into your infrastructure, ensuring top-tier security without distrupting operations or workflows.
            </p>
            <a href="#" className="text-[#004080] hover:underline">Learn More →</a>
          </div>

          <div className="bg-[#cce5ff] rounded-xl p-6 hover:shadow-lg transition">
            <div className="mb-4 flex justify-center">
              <div className="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow">
                <BarChart2 className="w-8 h-8 text-[#004080]" />
              </div>
            </div>
            <h3 className="text-xl font-semibold mb-2">Scalable & Adaptive</h3>
            <p className="text-[#00334d] mb-4">
              From small businesses to large enterprises, EYESHIELD scales with your needs, providing flexible,comprehensive protection as your oraganization grows.
            </p>
            <a href="#" className="text-[#004080] hover:underline">Learn More →</a>
          </div>
        </div>
      </div>
    </section>
  );
}
