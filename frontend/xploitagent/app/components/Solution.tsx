import Link from "next/link";

export default function Solution() {
  return (
    <section className="w-full  flex justify-center px-10 py-30">
      <div className="flex flex-col items-center justify-center">
        <div className="px-10 py-2 mb-7 bg-green-100/10 text-green-600 rounded-full tracking-widest">
          THERE IS A SOLUTION
        </div>
        <h2 className="text-5xl mb-2">
          Find Out All <span className="text-red-600">Vunerabilities</span>
        </h2>
        <p className="text-lg text-gray-400 mb-6">
          Outcomes delivered with world-class data, models, agents, and
          deployment.
        </p>
        <Link
          href={"#"}
          className="px-3 py-2 bg-green-800 hover:bg-green-500 hover:text-black font-bold rounded-md"
        >
          Try Now
        </Link>
      </div>
    </section>
  );
}
