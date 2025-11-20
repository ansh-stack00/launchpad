"use client";

import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faBars,
  faMagnifyingGlass,
  faUser,
  faXmark,
} from "@fortawesome/free-solid-svg-icons";

export default function Navbar({ classes = "" }) {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <header
      className={`bg-gradient-to-r from-slate-900 to-slate-800 shadow-lg px-6 py-4 rounded-xl ${classes}`}
    >
      <div className="flex justify-between items-center">
        {/* Logo + Hamburger */}
        <div className="flex items-center gap-4">
          {/* Mobile Menu Button */}
          <button
            className="md:hidden text-white text-2xl"
            onClick={() => setMenuOpen(!menuOpen)}
          >
            <FontAwesomeIcon icon={menuOpen ? faXmark : faBars} />
          </button>

          {/* Logo */}
          <div className="bg-gradient-to-r from-blue-600 to-blue-500 px-5 py-2 rounded-lg shadow-md">
            <h1 className="text-white font-semibold text-lg">Start BootStrap</h1>
          </div>
        </div>

        {/* Desktop Search + User */}
        <div className="hidden md:flex items-center gap-4">
          {/* Search Bar */}
          <div className="bg-slate-700 rounded-lg px-4 py-2 flex items-center gap-2 shadow-md hover:bg-slate-600 transition-colors">
            <input
              type="text"
              className="outline-none bg-transparent text-white placeholder-slate-400 w-48"
              placeholder="Search..."
            />
            <FontAwesomeIcon icon={faMagnifyingGlass} className="text-slate-300" />
          </div>

          {/* User */}
          <div className="bg-slate-700 rounded-full w-10 h-10 flex items-center justify-center hover:bg-slate-600 transition-colors cursor-pointer shadow-md">
            <FontAwesomeIcon icon={faUser} className="text-slate-200 text-lg" />
          </div>
        </div>
      </div>

      {/* MOBILE MENU */}
      {menuOpen && (
        <div className="mt-4 flex flex-col gap-4 md:hidden">
          {/* Search */}
          <div className="bg-slate-700 rounded-lg px-4 py-2 flex items-center gap-2 hover:bg-slate-600 transition-colors">
            <input
              type="text"
              className="outline-none bg-transparent text-white placeholder-slate-400 w-full"
              placeholder="Search..."
            />
            <FontAwesomeIcon icon={faMagnifyingGlass} className="text-slate-300" />
          </div>

          {/* User Button */}
          <div className="bg-slate-700 rounded-lg py-3 flex items-center justify-center gap-2 hover:bg-slate-600 transition-colors cursor-pointer shadow-md">
            <FontAwesomeIcon icon={faUser} className="text-slate-200 text-lg" />
            <span className="text-white text-sm">Profile</span>
          </div>
        </div>
      )}
    </header>
  );
}
