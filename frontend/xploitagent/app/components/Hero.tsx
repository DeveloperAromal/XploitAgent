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
        <source src="/videos/bg_video.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-t from-black via-black/50 z-10" />

      <div className="max-w-4xl z-40">
        <h1 className="text-6xl font-black pb-6">
          Next-Gen Autonomous Penetration Testing AI
        </h1>
        <p className="text-neutral-500 mb-5">
          Xploit Agent is the fastest way to automate end-to-end penetration
          testing—from initial reconnaissance to exploit delivery. The ultimate
          AI-powered offensive security partner.
        </p>
        <div className="action_buttons mb-8">
          <Link
            href={"#"}
            className="px-4 py-3 mr-3 rounded-md font-bold border-2 border-[var(--primary)] bg-[var(--primary)]  text-white"
          >
            Try Now
          </Link>
          <Link
            href={"#"}
            className="px-4 py-3 rounded-md font-bold border-2 border-[var(--primary)] hover:bg-[var(--primary)] transition-all duration-300"
          >
            Contact Us
          </Link>
        </div>
        <div className="demo_button bg-gray-500/30 px-3 py-2 rounded-full max-w-90 flex items-center">
          <div className="status text-white font-normal bg-[var(--primary)]/50 py-1 px-2 mr-4 rounded-full w-ful">
            New
          </div>
          <span className="text-gray-400 hover:text-[var(--primary)] transition-all duration-300">
            Check is your website safe or not ?
          </span>
        </div>
      </div>
    </section>
  );
}
