"use client";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faCode,
  faUsers,
  faBolt,
  faRocket,
} from "@fortawesome/free-solid-svg-icons";
import Navbar from "@/components/ui/Navbar";

export default function AboutPage() {

    
  return (
    <div className="p-10 text-white ">
        <Navbar classes=" rounded-3xl w-md lg:w-6xl mb-16 ml-6 lg:ml-64 px-16"/>
      {/* Hero Section */}
      <section className="mb-16">
        <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
          About Us
        </h1>
        <p className="text-lg text-slate-300 max-w-2xl">
          We help developers learn modern web development by building real
          projects using <strong>Next.js</strong>, <strong>TailwindCSS</strong>,
          and powerful UI systems.
        </p>
      </section>

      {/* Mission Section */}
      <section className="grid md:grid-cols-2 gap-10 mb-16">
        <div className="bg-white/5 p-8 rounded-2xl border border-white/10 backdrop-blur-sm">
          <h2 className="text-3xl font-bold mb-4 flex items-center gap-3">
            <FontAwesomeIcon icon={faRocket} className="text-pink-400 h-7" />
            Our Mission
          </h2>
          <p className="text-slate-300 leading-relaxed">
            Our mission is to empower developers with high-quality, structured
            learning paths that focus on real-world skills. We believe in
            hands-on education and building projects that matter.
          </p>
        </div>

        <div className="bg-white/5 p-8 rounded-2xl border border-white/10 backdrop-blur-sm">
          <h2 className="text-3xl font-bold mb-4 flex items-center gap-3">
            <FontAwesomeIcon icon={faBolt} className="text-yellow-300 h-7" />
            Why We Exist
          </h2>
          <p className="text-slate-300 leading-relaxed">
            Learning modern frameworks shouldn’t be confusing. We break down
            complex concepts into step-by-step lessons that blend theory with
            practice, helping you grow quickly.
          </p>
        </div>
      </section>

      {/* Highlights Section */}
      <section>
        <h2 className="text-4xl font-bold mb-10">What We Offer</h2>

        <div className="grid md:grid-cols-3 gap-8">
      
          <div className="bg-white/5 p-6 rounded-xl border border-white/10 hover:bg-white/10 transition">
            <FontAwesomeIcon
              icon={faCode}
              className="text-blue-400 text-3xl mb-4"
            />
            <h3 className="text-xl font-semibold mb-2">Modern Tech Stack</h3>
            <p className="text-slate-300 text-sm">
              Next.js, TailwindCSS, TypeScript, UI systems and real workflows.
            </p>
          </div>

       
          <div className="bg-white/5 p-6 rounded-xl border border-white/10 hover:bg-white/10 transition">
            <FontAwesomeIcon
              icon={faUsers}
              className="text-green-400 text-3xl mb-4"
            />
            <h3 className="text-xl font-semibold mb-2">Community Driven</h3>
            <p className="text-slate-300 text-sm">
              Join a community of learners and get feedback on your work.
            </p>
          </div>

          <div className="bg-white/5 p-6 rounded-xl border border-white/10 hover:bg-white/10 transition">
            <FontAwesomeIcon
              icon={faBolt}
              className="text-yellow-300 text-3xl mb-4"
            />
            <h3 className="text-xl font-semibold mb-2">Fast Learning</h3>
            <p className="text-slate-300 text-sm">
              Each course is structured for maximum speed and understanding.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
