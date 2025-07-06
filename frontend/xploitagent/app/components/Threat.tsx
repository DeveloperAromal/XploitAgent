export default function Threat() {
  return (
    <section className="flex flex-col md:flex-row items-start gap-6 px-10 py-10 bg-black text-white">
      <div>
        <div className="flex space-y-6">
          {/* Card: Threat Intelligence */}
          <div className="border-2 border-neutral-50 rounded-3xl p-6 shadow-lg bg-zinc-900">
            <h2 className="text-2xl font-bold text-neutral-400">
              Threat Intelligence
            </h2>
            <p className="text-zinc-300 mt-2">
              XPLOIT AGENT continuously analyzes your target's surface,
              gathering data from scrapers, subdomain enumerators, and stack
              detectors. Real-time insights are stored securely and can be
              reviewed or acted upon instantly.
            </p>
          </div>

          {/* Card: AI-Powered Analysis */}
          <div className="border-2 border-neutral-50 rounded-3xl p-6 shadow-lg bg-zinc-900">
            <h2 className="text-2xl font-bold text-neutral-400">
              AI-Powered Decision Engine
            </h2>
            <p className="text-zinc-300 mt-2">
              Leveraging advanced LLMs, XPLOIT AGENT interprets base scan
              outputs to recommend next attack vectors, identify stack
              weaknesses, and propose logical exploitation paths — all
              autonomously.
            </p>
          </div>
        </div>
        <div className="border-2 border-neutral-50 rounded-3xl p-6 shadow-lg bg-zinc-900">
          <h2 className="text-2xl font-bold text-neutral-400">
            AI-Powered Decision Engine
          </h2>
          <p className="text-zinc-300 mt-2">
            Leveraging advanced LLMs, XPLOIT AGENT interprets base scan outputs
            to recommend next attack vectors, identify stack weaknesses, and
            propose logical exploitation paths — all autonomously.
          </p>
        </div>
      </div>
    </section>
  );
}
