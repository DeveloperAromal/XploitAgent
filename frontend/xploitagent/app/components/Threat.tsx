export default function Threat() {
  return (
    <section className="flex items-center px-10 space-x-3">
      <div className="box_one w-1/2 h-80 bg-[var(--primary)]/20 rounded-lg p-10 ">
        <h2 className="text-9xl mb-3 font-semibold text-[var(--primary-text)]">
          80%
        </h2>
        <p className="text-5xl text-[var(--primary-dull-text)] ">
          of your website data is leaking like waterfall
        </p>
      </div>
      <div
        className="box_one w-1/2 h-80 bg-[var(--primary)]/20 rounded-lg p-10 bg-cover bg-center"
        style={{ backgroundImage: "url('/assets/scale.png')" }}
      >
        <p className="text-5xl text-[var(--primary-dull-text)] ">
          Beat the odds. <br /> Optimize your <br /> Security.
        </p>
      </div>
    </section>
  );
}
