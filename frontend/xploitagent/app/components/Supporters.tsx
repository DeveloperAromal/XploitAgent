"use client";
import Image from "next/image";

const logos = [
  "/brands/google.png",
  "/brands/meta.png",
  "/brands/google.png",
  "/brands/shopify.png",
  "/brands/shopify.png",
  "/brands/google.png",
  "/brands/meta.png",
  "/brands/shopify.png",
  "/brands/google.png",
  "/brands/meta.png",
  "/brands/google.png",
  "/brands/shopify.png",
  "/brands/shopify.png",
  "/brands/google.png",
  "/brands/meta.png",
  "/brands/shopify.png",
];

export default function BrandLoop() {
  return (
    <section className="relative w-full bg-black py-12 overflow-hidden">
      {/* Fade Overlays */}
      <div className="absolute left-0 top-0 h-full w-32 bg-gradient-to-r from-black to-transparent z-10 pointer-events-none" />
      <div className="absolute right-0 top-0 h-full w-32 bg-gradient-to-l from-black to-transparent z-10 pointer-events-none" />

      <div className="top text-center mb-8 ">
        <h2 className="font-semibold text-6xl mb-2.5">
          Brands Who Use Our Services
        </h2>
        <p className="text-gray-400">
          They use our service dusk-dawn, then why not you ?
        </p>
      </div>
      <div className="whitespace-nowrap animate-scroll flex items-center space-x-12">
        {logos.map((src, idx) => (
          <Image
            key={idx}
            src={src}
            alt={`logo-${idx}`}
            width={100}
            height={100}
            className="object-contain grayscale hover:grayscale-0 transition-all duration-300"
          />
        ))}
      </div>
    </section>
  );
}
