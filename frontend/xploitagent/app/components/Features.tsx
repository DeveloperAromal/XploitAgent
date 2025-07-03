"use client";

import { useState } from "react";
import Image from "next/image";

const items = [
  {
    key: "foundation",
    title: "Foundation Models",
    description:
      "Scale partners or integrates with all of the leading AI models, from open-source to closed-source, including OpenAI, Google, Meta, Cohere, and more.",
    image: "/images/foundation.png",
  },
  {
    key: "enterprise",
    title: "Enterprise Data",
    description:
      "Scale's Data Engine enables you to integrate your enterprise data into the fold of these models, providing the base for long-term strategic differentiation.",
    image: "/images/enterprise.png",
  },
  {
    key: "training",
    title: "Fine-Tuning and RLHF",
    description:
      "Adapt best-in-class foundation models to your business and your specific data to build sustainable, successful AI programs and data from your enterprise.",
    image: "/images/rlhf.png",
  },
];

export default function Features() {
  const [activeKey, setActiveKey] = useState("foundation");

  const activeItem = items.find((item) => item.key === activeKey);
  return (
    <section className="flex flex-col md:flex-row w-full bg-black text-white px-10 py-20 gap-10">
      {/* Left Content */}
      <div className="w-full md:w-1/2 space-y-8">
        {items.map((item) => (
          <div
            key={item.key}
            onMouseEnter={() => setActiveKey(item.key)}
            className={`transition-colors cursor-pointer ${
              activeKey === item.key ? "text-white" : "text-gray-500"
            }`}
          >
            <h3 className="text-xl font-semibold">{item.title}</h3>
            <p className="mt-1 text-sm max-w-md">{item.description}</p>
          </div>
        ))}
      </div>

      {/* Right Image */}
      <div className="w-full md:w-1/2 flex justify-center items-center">
        <Image
          src={activeItem?.image ?? ""}
          alt={activeItem?.title ?? ""}
          width={500}
          height={300}
          className="rounded-lg transition-all duration-500"
        />
      </div>
    </section>
  );
}
