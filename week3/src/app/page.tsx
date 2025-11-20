"use client"
import React, { useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faArrowRight,
  faCode,
  faTableCellsLarge, // instead of Layout
  faLayerGroup,     // instead of Layers
  faGlobe,
  faBolt,           // instead of Zap
  faBookOpen,
  faCircleCheck,    // instead of CheckCircle
  faStar
} from "@fortawesome/free-solid-svg-icons";

export default function LandingPage() {
  const [scrollY, setScrollY] = useState(0);
  const [activeDay, setActiveDay] = useState(null);

  useEffect(() => {
    const handleScroll = () => setScrollY(window.scrollY);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const days = [
    {
      day: 1,
      title: "TailwindCSS + UI System Basics",
      icon: <FontAwesomeIcon icon={faTableCellsLarge} className="w-8 h-8" />,
      topics: [
        "Install Tailwind in Next.js",
        "Utility classes, spacing, colors, fonts",
        "Custom theme configuration",
      ],
      exercise: "Build a Dashboard Layout skeleton (header + sidebar)",
      outputs: ["/app/layout.jsx", "/components/ui/Navbar.jsx", "/components/ui/Sidebar.jsx"],
      color: "from-blue-500 to-cyan-500",
    },
    {
      day: 2,
      title: "Tailwind Advanced + Component Library",
      icon: <FontAwesomeIcon icon={faLayerGroup} className="w-8 h-8" />,
      topics: [
        "Flex + Grid with Tailwind",
        "Components mindset (atomic design)",
        "Reusable components with props",
      ],
      exercise: "Build a component library (Button, Input, Card, Badge, Modal)",
      outputs: ["/components/ui/*", "UI-COMPONENT-DOCS.md"],
      color: "from-purple-500 to-pink-500",
    },
    {
      day: 3,
      title: "Next.js Routing + Layout System",
      icon: <FontAwesomeIcon icon={faGlobe} className="w-8 h-8" />,
      topics: [
        "Next.js routing system",
        "Nested layouts",
        "Shared navigation across pages",
        "Client vs Server Components",
      ],
      exercise: "Build multi-page structure with nested routing",
      outputs: ["/ (landing)", "/about", "/dashboard", "/dashboard/profile"],
      color: "from-orange-500 to-red-500",
    },
    {
      day: 4,
      title: "Dynamic UI + Image Optimization",
      icon: <FontAwesomeIcon icon={faBolt} className="w-8 h-8" />,
      topics: [
        "next/image (optimized image rendering)",
        "Responsive images + optimization",
        "Typography & SEO improvements",
        "Animations using Tailwind + Framer Motion",
      ],
      exercise: "Build a responsive landing page (SaaS product page)",
      outputs: ["/app/page.jsx", "screenshots/landing-page.png"],
      color: "from-emerald-500 to-teal-500",
      sections: ["Hero section", "Features grid", "Testimonials", "Footer"],
    },
    {
      day: 5,
      title: "Capstone Mini Project",
      icon: <FontAwesomeIcon icon={faBookOpen} className="w-8 h-8" />,
      topics: [
        "Full Multi-Page UI (No backend)",
        "Component reuse from /components/ui",
        "Clean routing structure",
        "Mobile responsive UI",
      ],
      exercise: "Build complete frontend application",
      outputs: ["week3-next-tailwind-frontend", "README.md with screenshots"],
      color: "from-pink-500 to-rose-500",
      sections: [
        "/login (form)",
        "/dashboard (cards/widgets)",
        "/dashboard/users (table)",
        "/dashboard/profile",
      ],
      isCapstone: true,
    },
  ];

  const features = [
    {
      icon: <FontAwesomeIcon icon={faBolt} className="w-6 h-6" />,
      title: "Fast-Paced",
      desc: "5 days of intensive learning",
    },
    {
      icon: <FontAwesomeIcon icon={faCode} className="w-6 h-6" />,
      title: "Hands-On",
      desc: "Build real-world projects",
    },
    {
      icon: <FontAwesomeIcon icon={faBookOpen} className="w-6 h-6" />,
      title: "Comprehensive",
      desc: "From basics to advanced",
    },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white overflow-hidden">
      {/* Animated Background Elements */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div
          className="absolute top-1/4 -left-20 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl"
          style={{ transform: `translateY(${scrollY * 0.3}px)` }}
        />
        <div
          className="absolute bottom-1/4 -right-20 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl"
          style={{ transform: `translateY(${-scrollY * 0.2}px)` }}
        />
      </div>

      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center justify-center px-6 py-20">
        <div className="max-w-6xl mx-auto text-center space-y-8 animate-fadeIn">
          <div className="inline-block">
            <div className="px-4 py-2 bg-gradient-to-r from-blue-500/20 to-purple-500/20 rounded-full border border-blue-500/30 backdrop-blur-sm mb-6 animate-slideDown">
              <span className="text-sm font-semibold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                5-Day Intensive Course
              </span>
            </div>
          </div>

          <h1 className="text-6xl md:text-7xl lg:text-8xl font-bold leading-tight animate-slideUp">
            Master{" "}
            <span className="bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
              Next.js
            </span>
            <br />& TailwindCSS
          </h1>

          <p
            className="text-xl md:text-2xl text-slate-300 max-w-3xl mx-auto animate-slideUp"
            style={{ animationDelay: "0.2s" }}
          >
            Build production-ready web applications with modern tools and best
            practices
          </p>

          <div
            className="flex flex-wrap gap-4 justify-center animate-slideUp"
            style={{ animationDelay: "0.4s" }}
          >
            <button className="group px-8 py-4 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg font-semibold text-lg hover:shadow-2xl hover:shadow-purple-500/50 transition-all duration-300 hover:scale-105 flex items-center gap-2">
              Start Learning
              <FontAwesomeIcon
                icon={faArrowRight}
                className="w-5 h-5 group-hover:translate-x-1 transition-transform"
              />
            </button>
            <button className="px-8 py-4 bg-white/10 backdrop-blur-sm rounded-lg font-semibold text-lg hover:bg-white/20 transition-all duration-300 border border-white/20">
              View Curriculum
            </button>
          </div>

          {/* Feature Pills */}
          <div
            className="flex flex-wrap gap-6 justify-center pt-8 animate-slideUp"
            style={{ animationDelay: "0.6s" }}
          >
            {features.map((feature, i) => (
              <div
                key={i}
                className="flex items-center gap-3 px-6 py-3 bg-white/5 backdrop-blur-sm rounded-full border border-white/10 hover:bg-white/10 transition-all duration-300"
              >
                <div className="text-blue-400">{feature.icon}</div>
                <div className="text-left">
                  <div className="font-semibold text-sm">{feature.title}</div>
                  <div className="text-xs text-slate-400">{feature.desc}</div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Scroll Indicator */}
        <div className="absolute bottom-10 left-1/2 -translate-x-1/2 animate-bounce">
          <div className="w-6 h-10 border-2 border-white/30 rounded-full flex justify-center">
            <div className="w-1 h-3 bg-white/50 rounded-full mt-2 animate-pulse" />
          </div>
        </div>
      </section>

      {/* Curriculum Section */}
      <section className="relative py-20 px-6">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16 space-y-4">
            <h2 className="text-5xl md:text-6xl font-bold">
              Your Learning{" "}
              <span className="bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                Journey
              </span>
            </h2>
            <p className="text-xl text-slate-300">
              Five intensive days to transform your skills
            </p>
          </div>

          <div className="space-y-8">
            {days.map((day) => (
              <div
                key={day.day}
                className="group relative bg-white/5 backdrop-blur-sm rounded-2xl border border-white/10 overflow-hidden hover:border-white/30 transition-all duration-500 hover:scale-[1.02]"
                onMouseEnter={() => setActiveDay(day.day)}
                onMouseLeave={() => setActiveDay(null)}
              >
                {/* Gradient Overlay */}
                <div
                  className={`absolute inset-0 bg-gradient-to-r ${day.color} opacity-0 group-hover:opacity-10 transition-opacity duration-500`}
                />

                <div className="relative p-8 md:p-10">
                  <div className="flex flex-col md:flex-row gap-6 md:gap-8">
                    {/* Day Number */}
                    <div className="flex-shrink-0">
                      <div
                        className={`w-20 h-20 rounded-2xl bg-gradient-to-br ${day.color} flex items-center justify-center transform group-hover:scale-110 group-hover:rotate-3 transition-all duration-300 ${
                          day.isCapstone ? "ring-4 ring-yellow-400/50" : ""
                        }`}
                      >
                        <div className="text-center relative">
                          {day.isCapstone && (
                            <FontAwesomeIcon
                              icon={faStar}
                              className="w-4 h-4 absolute -top-1 -right-1 text-yellow-400"
                            />
                          )}
                          <div className="text-xs font-semibold opacity-80">
                            DAY
                          </div>
                          <div className="text-3xl font-bold">{day.day}</div>
                        </div>
                      </div>
                    </div>

                    {/* Content */}
                    <div className="flex-grow space-y-6">
                      <div className="flex items-start gap-4">
                        <div
                          className={`p-3 rounded-xl bg-gradient-to-br ${day.color} bg-opacity-20`}
                        >
                          {day.icon}
                        </div>
                        <div>
                          <h3 className="text-2xl md:text-3xl font-bold mb-2 flex items-center gap-2">
                            {day.title}
                            {day.isCapstone && (
                              <span className="px-3 py-1 bg-yellow-400/20 text-yellow-400 text-xs font-bold rounded-full border border-yellow-400/30">
                                CAPSTONE
                              </span>
                            )}
                          </h3>
                          <p className="text-slate-400">
                            {day.isCapstone
                              ? "Final Project"
                              : "Master the essentials"}
                          </p>
                        </div>
                      </div>

                      <div className="grid md:grid-cols-2 gap-6">
                        {/* Topics */}
                        <div className="space-y-3">
                          <h4 className="text-sm font-semibold text-blue-400 uppercase tracking-wide">
                            Topics Covered
                          </h4>
                          <ul className="space-y-2">
                            {day.topics.map((topic, i) => (
                              <li
                                key={i}
                                className="flex items-start gap-2 text-slate-300"
                              >
                                <FontAwesomeIcon
                                  icon={faCircleCheck}
                                  className="w-5 h-5 text-green-400 flex-shrink-0 mt-0.5"
                                />
                                <span>{topic}</span>
                              </li>
                            ))}
                          </ul>
                        </div>

                        {/* Exercise & Outputs */}
                        <div className="space-y-4">
                          <div className="space-y-2">
                            <h4 className="text-sm font-semibold text-purple-400 uppercase tracking-wide">
                              Hands-On Exercise
                            </h4>
                            <p className="text-slate-300">{day.exercise}</p>
                          </div>

                          {day.sections && (
                            <div className="space-y-2">
                              <h4 className="text-sm font-semibold text-cyan-400 uppercase tracking-wide">
                                {day.isCapstone ? "Pages to Build" : "Sections"}
                              </h4>
                              <ul className="space-y-1">
                                {day.sections.map((section, i) => (
                                  <li
                                    key={i}
                                    className="flex items-center gap-2 text-sm text-slate-300"
                                  >
                                    <div className="w-1.5 h-1.5 rounded-full bg-cyan-400" />
                                    {section}
                                  </li>
                                ))}
                              </ul>
                            </div>
                          )}

                          <div className="space-y-2">
                            <h4 className="text-sm font-semibold text-pink-400 uppercase tracking-wide">
                              Deliverables
                            </h4>
                            <div className="flex flex-wrap gap-2">
                              {day.outputs.map((output, i) => (
                                <code
                                  key={i}
                                  className="px-3 py-1 bg-slate-800/80 rounded text-xs font-mono text-slate-300 border border-slate-700"
                                >
                                  {output}
                                </code>
                              ))}
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Progress Bar */}
                <div
                  className={`h-1 bg-gradient-to-r ${day.color} transform origin-left transition-transform duration-500 ${
                    activeDay === day.day ? "scale-x-100" : "scale-x-0"
                  }`}
                />
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="relative py-20 px-6">
        <div className="max-w-4xl mx-auto">
          <div className="relative bg-gradient-to-r from-blue-600 to-purple-600 rounded-3xl p-12 md:p-16 text-center space-y-6 overflow-hidden">
            <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImdyaWQiIHdpZHRoPSI2MCIgaGVpZ2h0PSI2MCIgcGF0dGVyblVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTSAxMCAwIEwgMCAwIDAgMTAiIGZpbGw9Im5vbmUiIHN0cm9rZT0id2hpdGUiIHN0cm9rZS1vcGFjaXR5PSIwLjEiIHN0cm9rZS13aWR0aD0iMSIvPjwvcGF0dGVybj48L2RlZnM+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0idXJsKCNncmlkKSIvPjwvc3ZnPg==')] opacity-30" />

            <div className="relative">
              <h2 className="text-4xl md:text-5xl font-bold mb-4">
                Ready to Start Building?
              </h2>
              <p className="text-xl text-blue-100 mb-8">
                Join hundreds of developers mastering modern web development
              </p>

              <button className="group px-10 py-5 bg-white text-blue-600 rounded-xl font-bold text-lg hover:shadow-2xl transition-all duration-300 hover:scale-105 inline-flex items-center gap-3">
                Enroll Now
                <FontAwesomeIcon
                  icon={faArrowRight}
                  className="w-6 h-6 group-hover:translate-x-2 transition-transform"
                />
              </button>

              <div className="mt-8 flex items-center justify-center gap-8 text-sm">
                <div className="flex items-center gap-2">
                  <FontAwesomeIcon icon={faCircleCheck} className="w-5 h-5" />
                  <span>5-Day Course</span>
                </div>
                <div className="flex items-center gap-2">
                  <FontAwesomeIcon icon={faCircleCheck} className="w-5 h-5" />
                  <span>Lifetime Access</span>
                </div>
                <div className="flex items-center gap-2">
                  <FontAwesomeIcon icon={faCircleCheck} className="w-5 h-5" />
                  <span>Project Files</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="relative py-10 px-6 border-t border-white/10">
        <div className="max-w-6xl mx-auto text-center text-slate-400">
          <p>© 2024 Next.js Learning Path. Built with Next.js & TailwindCSS</p>
        </div>
      </footer>

      <style jsx>{`
        @keyframes fadeIn {
          from {
            opacity: 0;
          }
          to {
            opacity: 1;
          }
        }

        @keyframes slideUp {
          from {
            opacity: 0;
            transform: translateY(30px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        @keyframes slideDown {
          from {
            opacity: 0;
            transform: translateY(-20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        .animate-fadeIn {
          animation: fadeIn 1s ease-out;
        }

        .animate-slideUp {
          animation: slideUp 0.8s ease-out backwards;
        }

        .animate-slideDown {
          animation: slideDown 0.6s ease-out;
        }
      `}</style>
    </div>
  );
}
