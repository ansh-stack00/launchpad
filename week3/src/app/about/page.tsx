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
    <div className="p-10 text-white">
      {/* Responsive Navbar */}
      <Navbar classes="rounded-3xl  mb-16 mr-2  " />

      {/* HERO SECTION WITH IMAGE */}
      <section className="relative w-full h-72 rounded-3xl overflow-hidden mb-16 shadow-lg">
        <img
          src="https://plus.unsplash.com/premium_photo-1685086785223-485f800ce410?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDl8fGNvZGluZ3xlbnwwfHwwfHx8MA%3D%3D"
          className="w-full h-full object-cover"
          alt="Programming background"
        />
        <div className="absolute inset-0 bg-gradient-to-r from-black/70 to-black/20 flex flex-col justify-center px-10">
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
            About Us
          </h1>
          <p className="text-lg text-slate-200 max-w-xl">
            We help developers grow by building real-world projects using
            Next.js, TailwindCSS, and modern UI systems.
          </p>
        </div>
      </section>

      {/* MISSION SECTION WITH IMAGE */}
      <section className="grid md:grid-cols-2 gap-10 mb-16">
        {/* Text Box */}
        <div className="bg-white/5 p-8 rounded-2xl border border-white/10 backdrop-blur-sm">
          <h2 className="text-3xl font-bold mb-4 flex items-center gap-3">
            <FontAwesomeIcon icon={faRocket} className="text-pink-400 h-7" />
            Our Mission
          </h2>
          <p className="text-slate-300 leading-relaxed">
            Our mission is to empower developers with structured learning paths
            that focus on real-world skills. We believe in hands-on practice and
            building projects that matter.
          </p>
        </div>

        {/* Image Box */}
        <div className="rounded-2xl overflow-hidden shadow-lg">
          <img
            src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1400&q=80"
            alt="Developers working"
            className="w-full h-full object-cover"
          />
        </div>
      </section>

      {/* WHY WE EXIST SECTION */}
      <section className="bg-white/5 p-8 rounded-2xl border border-white/10 backdrop-blur-sm mb-20">
        <h2 className="text-3xl font-bold mb-4 flex items-center gap-3">
          <FontAwesomeIcon icon={faBolt} className="text-yellow-300 h-7" />
          Why We Exist
        </h2>
        <p className="text-slate-300 leading-relaxed">
          Learning modern frameworks shouldn’t feel confusing. We simplify the
          entire process by breaking down difficult concepts into easy,
          step-by-step lessons supported by real projects.
        </p>
      </section>

      {/* WHAT WE OFFER SECTION */}
      <section>
        <h2 className="text-4xl font-bold mb-10">What We Offer</h2>

        <div className="grid md:grid-cols-3 gap-8">
          {/* Card 1 */}
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

          {/* Card 2 */}
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

          {/* Card 3 */}
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
