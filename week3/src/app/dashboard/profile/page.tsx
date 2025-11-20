"use client";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faUser,
  faEnvelope,
  faBriefcase,
  faPenToSquare,
  faLocationDot,
  faCalendar,
} from "@fortawesome/free-solid-svg-icons";



export default function ProfilePage() {
  return (
    <div className=" text-white ">

      {/* Banner */}
      <section className="relative w-full h-64 rounded-3xl overflow-hidden shadow-lg mb-8">
        <img
          src="https://images.unsplash.com/photo-1503264116251-35a269479413?auto=format&fit=crop&w=1600&q=80"
          className="w-full h-full object-cover"
          alt="Banner"
        />
        <div className="absolute inset-0 bg-gradient-to-r from-black/70 to-black/30"></div>

        {/* Avatar */}
        <div className="absolute -bottom-9 left-10">
          <img
            src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?auto=format&fit=crop&w=400&q=80"
            className="w-32 h-32 rounded-full border-4 border-white shadow-xl object-cover"
            alt="User avatar"
          />
        </div>
      </section>

      {/* Profile Info */}
      <section className="ml-2 lg:ml-16 p-5">
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-10">
          <div>
            <h1 className="text-4xl font-bold">John Doe</h1>
            <p className="text-slate-400 mt-1">@john_doe_dev</p>
          </div>

          <button className="mt-4 md:mt-0 bg-blue-600 hover:bg-blue-500 transition px-5 py-2 rounded-lg flex items-center gap-2 shadow-md">
            <FontAwesomeIcon icon={faPenToSquare} />
            Edit Profile
          </button>
        </div>

        {/* Information Blocks */}
        <div className="grid md:grid-cols-2 gap-8 mb-16">
          <div className="bg-white/5 p-6 rounded-2xl backdrop-blur-md border border-white/10">
            <h2 className="text-xl font-semibold mb-4">Personal Info</h2>

            <div className="space-y-3 text-slate-300">
              <p className="flex items-center gap-3">
                <FontAwesomeIcon icon={faUser} className="text-blue-400" />
                John Doe
              </p>
              <p className="flex items-center gap-3">
                <FontAwesomeIcon icon={faEnvelope} className="text-green-400" />
                john@example.com
              </p>
              <p className="flex items-center gap-3">
                <FontAwesomeIcon icon={faBriefcase} className="text-pink-400" />
                Full Stack Developer
              </p>
              <p className="flex items-center gap-3">
                <FontAwesomeIcon
                  icon={faLocationDot}
                  className="text-yellow-300"
                />
                San Francisco, USA
              </p>
              <p className="flex items-center gap-3">
                <FontAwesomeIcon icon={faCalendar} className="text-purple-400" />
                Joined: Jan 2022
              </p>
            </div>
          </div>

          <div className="bg-white/5 p-6 rounded-2xl backdrop-blur-md border border-white/10">
            <h2 className="text-xl font-semibold mb-4">About Me</h2>
            <p className="text-slate-300 leading-relaxed">
              Passionate full-stack developer with a love for building modern,
              scalable web applications. Skilled in Next.js, TypeScript,
              TailwindCSS, and cloud deployments. Always learning, always
              coding!
            </p>
          </div>
        </div>

        {/* Stats Section */}
        <h2 className="text-3xl font-bold mb-6">Stats</h2>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
          <div className="bg-white/5 p-6 rounded-xl border border-white/10 text-center hover:bg-white/10 transition">
            <h3 className="text-3xl font-bold">128</h3>
            <p className="text-slate-300 mt-1">Projects</p>
          </div>

          <div className="bg-white/5 p-6 rounded-xl border border-white/10 text-center hover:bg-white/10 transition">
            <h3 className="text-3xl font-bold">4.9</h3>
            <p className="text-slate-300 mt-1">Rating</p>
          </div>

          <div className="bg-white/5 p-6 rounded-xl border border-white/10 text-center hover:bg-white/10 transition">
            <h3 className="text-3xl font-bold">52k</h3>
            <p className="text-slate-300 mt-1">Followers</p>
          </div>

          <div className="bg-white/5 p-6 rounded-xl border border-white/10 text-center hover:bg-white/10 transition">
            <h3 className="text-3xl font-bold">22</h3>
            <p className="text-slate-300 mt-1">Badges</p>
          </div>
        </div>
      </section>
    </div>
  );
}
