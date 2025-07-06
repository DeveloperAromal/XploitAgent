import Link from "next/link";

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
        <h2 className="text-8xl font-semibold mb-40">
          Lightning fast. <br /> Edge ready
        </h2>
        <pre className="text-sm mb-7 text-white bg-gray-900  p-4 rounded-md overflow-x-auto">
          <code>
            {`import { neon } from '@neondatabase/serverless';

const sql = neon('postgresql://usr:pass@proj.us-east-2.aws.neon.tech/db');

const posts = await sql('SELECT * FROM posts');`}
          </code>
        </pre>
        <Link href={"#"} className="text-gray-500 hover:text-blue-600">
          Test Your Website Now
        </Link>
      </div>
    </section>
  );
}
