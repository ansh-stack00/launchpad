"use client";
import React from "react";

interface CardProps {
  title: string;
  colorClass: string;
  onViewDetails: () => void;
}

export default function Card({ title, colorClass, onViewDetails } : CardProps) {
  return (
    <div
      className={`
        ${colorClass}
        w-80 h-36 p-6 rounded-md text-white
        flex flex-col justify-between
        transform transition-all duration-300 cursor-pointer
        hover:scale-105 hover:-translate-y-1 hover:shadow-xl
        
      `}
    >
      <h3 className="text-lg font-semibold">{title}</h3>
    <br className="text-amber-50"></br>
      <button
        onClick={onViewDetails}
        className="mt-6 font-medium flex items-center gap-1 group"
      >
        View Details
        <span className="transition-all duration-300 group-hover:translate-x-1">
          →
        </span>
      </button>
    </div>
  );
}
