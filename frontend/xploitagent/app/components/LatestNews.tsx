import Image from "next/image";

export default function LatestNews() {
  return (
    <section className="flex items-center px-10 py-10">
      <div className="news_box bg-[var(--primary)]/30 p-20 rounded-lg flex items-start space-x-20">
        <div className="left w-1/3">
          <h2 className="text-2xl font-bold text-[var(--primary-text)] bg-[var(--primary)]/40 mb-6 py-2 px-2 rounded-full max-w-50 text-center">
            Latest News
          </h2>
          <h4 className="text-2xl font-bold text-[var(--primary-text)]">
            Major Breaches in 2024 Could Have Been Prevented with Proactive
            Testing
          </h4>
        </div>
        <div className="right w-2/3 flex items-center space-x-12">
          <p className="text-[var(--primary-text)]">
            The Snowflake compromise affected 560 million customers across
            companies like Ticketmaster, while cybersecurity teams become
            increasingly overwhelmed. With losses expected to hit $10.5 trillion
            by 2025, organizations need autonomous AI solutions that
            continuously identify vulnerabilities before attackers exploit them,
            rather than responding after breaches occur.
          </p>
          <Image
            src={"/assets/mock_one.png"}
            alt="image"
            width={250}
            height={250}
          />
        </div>
      </div>
    </section>
  );
}
