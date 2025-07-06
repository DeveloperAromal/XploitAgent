import Link from "next/link";

export default function Hero() {
  return (
    <section className="h-screen flex items-center px-10">
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute top-0 left-0 w-full h-full object-cover z-0 opacity-33 "
      >
        <source src="/assets/hero-video.webm" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-t from-black via-black/50 z-10" />

      <div className="max-w-3xl z-40">
        <h1 className="text-7xl pb-6">
          Next-Gen Autonomous Penetration Testing AI
        </h1>
        <p className="text-neutral-500 mb-10">
          Xploit Agent is the fastest way to automate end-to-end penetration
          testing—from initial reconnaissance to exploit delivery. The ultimate
          AI-powered offensive security partner.
        </p>
        <div className="action_buttons flex gap-6">
          <Link
            href={"#"}
            className="px-16 py-4  rounded-lg font-bold border-2 bg-white  text-neutral-900"
          >
            <code>Try Now</code>
          </Link>
          <Link
            href={"#"}
            className="px-10 py-4 rounded-lg font-bold border-2 border-white hover:bg-white hover:text-neutral-900 transition-all duration-300"
          >
            <code> Contact Us</code>
          </Link>
        </div>
      </div>
    </section>
  );
}
