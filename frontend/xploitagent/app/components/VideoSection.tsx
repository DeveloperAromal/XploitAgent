import { Radar, FileBarChart2, Wrench } from "lucide-react";
import Link from "next/link";

export default function VideoSection() {
  return (
    <section className=" flex flex-col items-center pt-30 px-10">
      <div className="top text-center mb-16">
        <h2 className="font-semibold text-6xl mb-2.5">
          Shut your Mouth & Watch This
        </h2>
        <p className="text-gray-400">
          Science says that watching a video can make you understand more
        </p>
      </div>
      <div className="bottom flex items-start space-x-10">
        <div className="video_container">
          <iframe
            className="rounded-md"
            width="560"
            height="315"
            src="https://www.youtube.com/embed/_uQrJ0TkZlc?si=LtzUA0_izlm7t2xL"
            title="YouTube video player"
            frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            referrerPolicy="strict-origin-when-cross-origin"
            allowFullScreen
          ></iframe>
        </div>
        <div className="content_container">
          <h3 className="text-4xl mb-2">A Complete Manual Hand Made Guide</h3>
          <p className="text-gray-400 mb-6">
            watch this for a complete understanding
          </p>
          <ul className="mb-12 space-y-4 text-gray-300  text-sm">
            <li className="flex items-center space-x-3 hover:text-[var(--primary)]">
              <Radar className="w-5 h-5 " />
              <span className="">Real-Time Threat Detection</span>
            </li>
            <li className="flex items-center space-x-3 hover:text-[var(--primary)]">
              <FileBarChart2 className="w-5 h-5 " />
              <span className="">Automated Security Reports</span>
            </li>
            <li className="flex items-center space-x-3 hover:text-[var(--primary)]">
              <Wrench className="w-5 h-5 " />
              <span className="">Smart Fix Assistant</span>
            </li>
          </ul>
          <Link
            href={"#"}
            className="px-4 py-3 mr-3 rounded-md font-bold border-2 border-[var(--primary)] bg-[var(--primary)]  text-white"
          >
            Learn More
          </Link>
        </div>
      </div>
    </section>
  );
}
