import Image from "next/image";
import Link from "next/link";

export default function Navbar() {
  return (
    <header className="fixed w-full py-8 bg-black z-1000">
      <div>
        <nav className="flex justify-between items-center px-10">
          <div className="flex items-center justify-center gap-[3rem]">
            <Link
              href="#"
              className="text-cyan-400 flex items-center justify-center"
            >
              <h1>
                <Image
                  src="/assets/logo.png"
                  alt="logo"
                  width={40}
                  height={240}
                />
              </h1>
            </Link>
          </div>
          <div>
            <ul className="flex gap-[3rem] h-auto justify-center">
              <Link href="#" className="hover:text-cyan-400">
                <li>Features</li>
              </Link>
              <Link href="#" className="hover:text-cyan-400">
                <li>Resources</li>
              </Link>
              <Link href="#" className="hover:text-cyan-400">
                <li>Pricing</li>
              </Link>
              <Link href="#" className="hover:text-cyan-400">
                <li>Enterprise</li>
              </Link>
            </ul>
          </div>

          <div>
            <Link href="#">Contact sales</Link>
          </div>
        </nav>
      </div>
    </header>
  );
}
