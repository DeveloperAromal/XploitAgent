export default function VidSec() {
  return (
    <section className="h-screen relative flex items-start px-10 mt-[20rem]">
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute z-10 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-200 h-auto"
      >
        <source src="/assets/phone-active.mp4" type="video/mp4" />
        <source src="/assets/phone-active.webm" type="video/webm" />
      </video>

      <div className="relative -top-40 z-50 left-40">
        <h2 className="text-[7rem] max-w-4xl  line-height text-transparent bg-clip-text bg-gradient-to-tr from-white via-zinc-600 to-neutral-800">
          Lightning fast. Edge ready
        </h2>
      </div>
    </section>
  );
}
