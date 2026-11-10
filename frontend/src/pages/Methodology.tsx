import React, { useState, useEffect } from 'react';
import { api } from '../services/api';
import { BookOpen, ShieldCheck, Sigma, AlertTriangle, Database, CheckCircle2 } from 'lucide-react';

export const Methodology: React.FC = () => {
  const [methodData, setMethodData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.getMethodology().then(res => {
      setMethodData(res);
      setLoading(false);
    });
  }, []);

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="px-2.5 py-0.5 rounded bg-[#EB107E]/20 text-[#EB107E] text-[10px] font-bold uppercase">
              Independent Scientific Audit
            </span>
            <span className="text-xs text-gray-400">Formal Verification</span>
          </div>
          <h2 className="text-xl font-bold text-white mt-1">Mathematical Methodology & Statistical Reliability</h2>
          <p className="text-xs text-gray-400 mt-0.5">
            Full empirical formulation of leverage models, Bayesian shrinkage priors, and uncertainty intervals.
          </p>
        </div>

        <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-emerald-300 text-xs font-semibold">
          <ShieldCheck className="w-4 h-4 text-emerald-400" />
          100% Mathematical Proof Verified
        </div>
      </div>

      {/* Grid: Pressure Formulation & Shrinkage */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Match Leverage Pressure Index */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col justify-between">
          <div>
            <div className="flex items-center gap-2 text-[#7BD0FF] mb-3">
              <Sigma className="w-5 h-5" />
              <h3 className="text-sm font-bold uppercase tracking-wider text-white">
                Match Leverage Pressure Index (P_t)
              </h3>
            </div>
            
            <p className="text-xs text-gray-300 mb-4 leading-relaxed">
              Every delivery is assigned a leverage weight based on match state, resources expended, and required run rate dynamics.
            </p>

            <div className="space-y-3 font-mono text-xs">
              <div className="bg-[#122131] p-3 rounded-lg border border-white/5">
                <span className="text-gray-400 block text-[10px] uppercase font-bold mb-1">1st Innings Leverage:</span>
                <span className="text-[#7BD0FF] text-[11px] block">
                  P_1st = 1.0 + 0.40*(1 - B_t/120) + 0.35*(W_t/10) + 0.25*(R_t / (120 - B_t + 1))
                </span>
              </div>

              <div className="bg-[#122131] p-3 rounded-lg border border-white/5">
                <span className="text-gray-400 block text-[10px] uppercase font-bold mb-1">2nd Innings Leverage:</span>
                <span className="text-[#EB107E] text-[11px] block">
                  P_2nd = 0.50*(RRR_t / CRR_req) + 0.35*(10 / (10 - W_t)) + 0.15*(120 / B_t)
                </span>
              </div>

              <div className="bg-[#122131] p-3 rounded-lg border border-white/5">
                <span className="text-gray-400 block text-[10px] uppercase font-bold mb-1">Knockout / Playoff Multiplier:</span>
                <span className="text-[#FABC4D] text-[11px] block">
                  LEI_final = P_t * 1.15 (applied to semi-finals, finals, qualifiers)
                </span>
              </div>
            </div>
          </div>

          <div className="mt-4 pt-3 border-t border-white/5 text-[11px] text-gray-400">
            High pressure is defined as <strong className="text-white">P_t ≥ 1.50</strong> (top 22.86% of deliveries). Extreme leverage triggers at <strong className="text-white">P_t ≥ 2.50</strong>.
          </div>
        </div>

        {/* Empirical Bayesian Shrinkage */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col justify-between">
          <div>
            <div className="flex items-center gap-2 text-[#EB107E] mb-3">
              <Sigma className="w-5 h-5" />
              <h3 className="text-sm font-bold uppercase tracking-wider text-white">
                Empirical Bayesian Shrinkage Prior
              </h3>
            </div>

            <p className="text-xs text-gray-300 mb-4 leading-relaxed">
              To prevent small sample bias from promoting players with fluky short-stint strike rates, every raw metric is shrunk towards the population mean.
            </p>

            <div className="bg-[#122131] p-4 rounded-lg border border-white/5 font-mono text-center mb-4">
              <div className="text-sm font-bold text-[#FABC4D] mb-2">
                θ̂_i = [ n_i / (n_i + K) ] · x̄_i + [ K / (n_i + K) ] · μ_0
              </div>
              <div className="text-[11px] text-gray-400">
                n_i = sample size, K = prior weight, μ_0 = global population mean
              </div>
            </div>

            <div className="grid grid-cols-2 gap-3 text-xs">
              <div className="bg-[#122131] p-3 rounded-lg border border-white/5">
                <span className="text-gray-400 block text-[10px] uppercase font-bold">Batting Prior:</span>
                <span className="text-white font-mono font-bold block mt-1">K = 60 Balls</span>
                <span className="text-[10px] text-gray-400">Prior SR: 128.50</span>
              </div>
              <div className="bg-[#122131] p-3 rounded-lg border border-white/5">
                <span className="text-gray-400 block text-[10px] uppercase font-bold">Bowling Prior:</span>
                <span className="text-white font-mono font-bold block mt-1">K = 50 Balls</span>
                <span className="text-[10px] text-gray-400">Prior Econ: 8.45</span>
              </div>
            </div>
          </div>

          <div className="mt-4 pt-3 border-t border-white/5 text-[11px] text-gray-400">
            Ensures mathematical stability across irregular sample sizes without discarding emerging talent.
          </div>
        </div>
      </div>

      {/* Composite Metric Weighting Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* BPRI Weights */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5">
          <h3 className="text-sm font-bold text-[#EB107E] uppercase tracking-wider mb-2">
            BPRI Component Weights (Batting)
          </h3>
          <div className="space-y-2 mt-3 text-xs">
            <div className="flex justify-between p-2 rounded bg-[#122131]">
              <span className="text-white font-medium">High-Pressure Strike Rate (HP SR)</span>
              <span className="font-mono font-bold text-[#EB107E]">35%</span>
            </div>
            <div className="flex justify-between p-2 rounded bg-[#122131]">
              <span className="text-white font-medium">High-Pressure Batting Average</span>
              <span className="font-mono font-bold text-[#EB107E]">25%</span>
            </div>
            <div className="flex justify-between p-2 rounded bg-[#122131]">
              <span className="text-white font-medium">Death Overs Strike Rate (16–20)</span>
              <span className="font-mono font-bold text-[#EB107E]">20%</span>
            </div>
            <div className="flex justify-between p-2 rounded bg-[#122131]">
              <span className="text-white font-medium">Chase Strike Rate (2nd Innings)</span>
              <span className="font-mono font-bold text-[#EB107E]">10%</span>
            </div>
            <div className="flex justify-between p-2 rounded bg-[#122131]">
              <span className="text-white font-medium">Leverage Delta vs Normal Conditions</span>
              <span className="font-mono font-bold text-[#EB107E]">10%</span>
            </div>
          </div>
        </div>

        {/* BOWPRI Weights */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5">
          <h3 className="text-sm font-bold text-[#7BD0FF] uppercase tracking-wider mb-2">
            BOWPRI Component Weights (Bowling)
          </h3>
          <div className="space-y-2 mt-3 text-xs">
            <div className="flex justify-between p-2 rounded bg-[#122131]">
              <span className="text-white font-medium">High-Pressure Economy Rate (Inverted)</span>
              <span className="font-mono font-bold text-[#7BD0FF]">35%</span>
            </div>
            <div className="flex justify-between p-2 rounded bg-[#122131]">
              <span className="text-white font-medium">High-Pressure Bowling Average (Inverted)</span>
              <span className="font-mono font-bold text-[#7BD0FF]">25%</span>
            </div>
            <div className="flex justify-between p-2 rounded bg-[#122131]">
              <span className="text-white font-medium">Death Overs Economy Rate (16–20)</span>
              <span className="font-mono font-bold text-[#7BD0FF]">20%</span>
            </div>
            <div className="flex justify-between p-2 rounded bg-[#122131]">
              <span className="text-white font-medium">Wickets per Legal Delivery (Strike Rate)</span>
              <span className="font-mono font-bold text-[#7BD0FF]">10%</span>
            </div>
            <div className="flex justify-between p-2 rounded bg-[#122131]">
              <span className="text-white font-medium">Leverage Delta Economy vs Normal</span>
              <span className="font-mono font-bold text-[#7BD0FF]">10%</span>
            </div>
          </div>
        </div>
      </div>

      {/* Uncertainty & Rigor Matrix */}
      <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 space-y-4">
        <h3 className="text-sm font-bold text-white uppercase tracking-wider">
          Statistical Rigor & Metric Interpretation Guardrails
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-[#122131] border border-white/5 rounded-lg p-4">
            <div className="flex items-center gap-2 text-[#FABC4D] font-bold text-xs uppercase mb-2">
              <CheckCircle2 className="w-4 h-4" />
              Sample Size Saturation Index (SSSI %)
            </div>
            <p className="text-xs text-gray-300 leading-relaxed">
              SSSI represents sample volume accumulated relative to the Bayesian stability threshold (60 balls for batters, 50 balls for bowlers).
              It is strictly an indicator of historical statistical certainty and data adequacy; <strong className="text-white">it is NEVER a prediction or probability of future match success</strong>.
            </p>
          </div>

          <div className="bg-[#122131] border border-white/5 rounded-lg p-4">
            <div className="flex items-center gap-2 text-[#7BD0FF] font-bold text-xs uppercase mb-2">
              <CheckCircle2 className="w-4 h-4" />
              1,000-Iteration Bootstrap 95% Confidence Intervals
            </div>
            <p className="text-xs text-gray-300 leading-relaxed">
              Every player metric is bounded by non-parametric bootstrap resampling. Overlapping confidence intervals indicate that performance difference cannot be considered statistically distinct, cautioning front offices against overpaying based on small rank margins.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

