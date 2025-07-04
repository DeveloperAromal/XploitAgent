import { Twitter, Github, Facebook, Dribbble } from "lucide-react";

export default function Footer() {
  return (
    <footer className="bg-[var(--tertiary)] text-[var(--primary-text)] px-10 py-16">
      {/* Top Grid */}
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-10 border-b border-[var(--primary-dull-text)] pb-10">
        {/* ABOUT */}
        <div>
          <h3 className="text-white font-semibold mb-4">ABOUT</h3>
          <ul className="space-y-2 text-sm">
            <li>
              <a href="#">About</a>
            </li>
            <li>
              <a href="#">Submit an issue</a>
            </li>
            <li>
              <a href="#">GitHub Repo</a>
            </li>
            <li>
              <a href="#">Slack</a>
            </li>
          </ul>
        </div>

        {/* GETTING STARTED */}
        <div>
          <h3 className="text-white font-semibold mb-4">GETTING STARTED</h3>
          <ul className="space-y-2 text-sm">
            <li>
              <a href="#">Introduction</a>
            </li>
            <li>
              <a href="#">Documentation</a>
            </li>
            <li>
              <a href="#">Usage</a>
            </li>
            <li>
              <a href="#">Globals</a>
            </li>
            <li>
              <a href="#">Elements</a>
            </li>
            <li>
              <a href="#">Collections</a>
            </li>
            <li>
              <a href="#">Themes</a>
            </li>
          </ul>
        </div>

        {/* RESOURCES */}
        <div>
          <h3 className="text-white font-semibold mb-4">RESOURCES</h3>
          <ul className="space-y-2 text-sm">
            <li>
              <a href="#">API</a>
            </li>
            <li>
              <a href="#">Form Validations</a>
            </li>
            <li>
              <a href="#">Visibility</a>
            </li>
            <li>
              <a href="#">Accessibility</a>
            </li>
            <li>
              <a href="#">Community</a>
            </li>
            <li>
              <a href="#">Design Defined</a>
            </li>
            <li>
              <a href="#">Marketplace</a>
            </li>
          </ul>
        </div>

        {/* SOCIAL MEDIA */}
        <div>
          <h3 className="text-white font-semibold mb-4">SOCIAL MEDIA</h3>
          <p className="text-sm mb-4 text-white">
            Follow us on social media to find out the latest updates on our
            progress.
          </p>
          <div className="flex space-x-4 text-[var(--primary-text)]">
            <a href="#">
              <Twitter className="w-5 h-5 hover:text-white" />
            </a>
            <a href="#">
              <Github className="w-5 h-5 hover:text-white" />
            </a>
            <a href="#">
              <Facebook className="w-5 h-5 hover:text-white" />
            </a>
            <a href="#">
              <Dribbble className="w-5 h-5 hover:text-white" />
            </a>
          </div>
        </div>
      </div>

      {/* Bottom Line */}
      <div className="max-w-7xl mx-auto mt-8 flex flex-col md:flex-row justify-between items-center text-xs text-white">
        <p>© 2024 XploitAgent. All rights reserved.</p>
        <div className="flex flex-wrap space-x-4 mt-4 md:mt-0">
          <a href="#">Terms of Service</a>
          <a href="#">Privacy Policy</a>
          <a href="#">Security</a>
          <a href="#">Sitemap</a>
        </div>
        <div className="mt-4 md:mt-0">
          <select className="bg-transparent border-none text-sm outline-none">
            <option>English</option>
          </select>
        </div>
      </div>
    </footer>
  );
}
