// import Link from "next/link";

export default function VidSec() {
  return (
    <section className="h-screen relative flex items-start px-10 mt-50">
      <video
        autoPlay
        loop
        muted
        playsInline
        className="absolute z-10 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-250 h-auto"
      >
        <source src="/assets/phone.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <div className="top z-50">
        <h2 className="text-[5rem] font-extrabold mb-40">
          Lightning fast. <br /> Edge ready
        </h2>

        {/* <Link href={"#"} className="text-gray-500 hover:text-blue-600">
          Test Your Website Now
        </Link> */}
      </div>
    </section>
  );
}
