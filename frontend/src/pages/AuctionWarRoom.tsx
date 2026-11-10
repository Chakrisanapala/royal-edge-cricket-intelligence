import React, { useState, useEffect } from 'react';
import { api } from '../services/api';
import { 
  Gavel, 
  Wallet, 
  AlertTriangle, 
  CheckCircle2, 
  RefreshCw, 
  ShieldAlert, 
  Users, 
  Globe 
} from 'lucide-react';

export const AuctionWarRoom: React.FC = () => {
  const [totalBudget, setTotalBudget] = useState(42.80);
  const [targets, setTargets] = useState<any[]>([]);
  const [bids, setBids] = useState<Record<string, number>>({
    'Ashutosh Sharma': 8.50,
    'Shashank Singh': 7.00,
    'Matthew Humphreys': 4.20,
    'George Linde': 3.80
  });

  const [simulation, setSimulation] = useState<any>(null);

  useEffect(() => {
    api.getAuctionTargets().then(res => {
      setTargets(res);
    });
  }, []);

  useEffect(() => {
    api.simulateAuction(totalBudget, bids).then(res => {
      setSimulation(res);
    });
  }, [totalBudget, bids]);

  const handleBidChange = (name: string, value: number) => {
    setBids(prev => ({
      ...prev,
      [name]: Number(value)
    }));
  };

  const handleReset = () => {
    setBids({
      'Ashutosh Sharma': 8.50,
      'Shashank Singh': 7.00,
      'Matthew Humphreys': 4.20,
      'George Linde': 3.80
    });
  };

  const totalAllocated = Object.values(bids).reduce((a, b) => a + b, 0);
  const remainingPurse = totalBudget - totalAllocated;

  return (
    <div className="space-y-6">
      {/* Header & Policy Segregation Banner */}
      <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="px-2.5 py-0.5 rounded bg-[#FABC4D]/20 text-[#FABC4D] text-[10px] font-bold uppercase">
              Rajasthan Royals Strategy
            </span>
            <span className="text-xs text-gray-400">IPL 2027 Mega Auction</span>
          </div>
          <h2 className="text-xl font-bold text-white mt-1">Auction War Room & Purse Simulator</h2>
          <p className="text-xs text-gray-400 mt-0.5">
            Test bidding scenarios against simulated budget limits without compromising overseas quotas.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={handleReset}
            className="px-3.5 py-2 bg-[#1C2B3C] hover:bg-[#273647] text-white text-xs font-semibold rounded-lg flex items-center gap-1.5 transition-all"
          >
            <RefreshCw className="w-3.5 h-3.5 text-gray-400" />
            Reset to Recommendations
          </button>
        </div>
      </div>

      {/* Mandatory Policy Segregation Box */}
      <div className="bg-[#051424] border border-amber-500/30 rounded-xl p-4 flex items-start gap-3">
        <ShieldAlert className="w-5 h-5 text-[#FABC4D] shrink-0 mt-0.5" />
        <div className="text-xs text-gray-300 leading-relaxed">
          <span className="text-[#FABC4D] font-bold uppercase">Strict Policy Segregation Mandate: </span>
          Benchmark players (e.g., Mohammad Nawaz, Abrar Ahmed, Imad Wasim, Sufiyan Muqeem) serve solely as non-parametric Bayesian prior calibrations for high-pressure models. They hold <span className="text-red-400 font-bold">zero auction bidding eligibility</span>. Actionable bidding pipelines operate exclusively within the registered BCCI-eligible pool.
        </div>
      </div>

      {/* War Room Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Allocated Budget */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4 flex flex-col justify-between">
          <div className="flex items-center justify-between text-gray-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Simulated Outlay</span>
            <Wallet className="w-4 h-4 text-[#EB107E]" />
          </div>
          <div className="mt-3">
            <div className="text-3xl font-extrabold text-[#EB107E] font-mono">₹{totalAllocated.toFixed(2)} Cr</div>
            <div className="text-[11px] text-gray-400 mt-1">4 Targeted Acquisitions</div>
          </div>
        </div>

        {/* Remaining Purse */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4 flex flex-col justify-between">
          <div className="flex items-center justify-between text-gray-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Remaining Purse</span>
            <Gavel className="w-4 h-4 text-[#FABC4D]" />
          </div>
          <div className="mt-3">
            <div className={`text-3xl font-extrabold font-mono ${remainingPurse >= 0 ? 'text-[#FABC4D]' : 'text-red-400'}`}>
              ₹{remainingPurse.toFixed(2)} Cr
            </div>
            <div className="text-[11px] text-gray-400 mt-1">Target Purse: ₹{totalBudget.toFixed(2)} Cr</div>
          </div>
        </div>

        {/* Overseas Slot Status */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4 flex flex-col justify-between">
          <div className="flex items-center justify-between text-gray-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Overseas Quota</span>
            <Globe className="w-4 h-4 text-[#7BD0FF]" />
          </div>
          <div className="mt-3">
            <div className="text-3xl font-extrabold text-white font-mono">
              {simulation ? simulation.slots_impact.overseas_slots_available : '3 of 8 free'}
            </div>
            <div className="text-[11px] text-gray-400 mt-1">Max 8 Overseas Players Allowed</div>
          </div>
        </div>

        {/* Squad Slots Available */}
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-4 flex flex-col justify-between">
          <div className="flex items-center justify-between text-gray-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Squad Roster</span>
            <Users className="w-4 h-4 text-emerald-400" />
          </div>
          <div className="mt-3">
            <div className="text-3xl font-extrabold text-white font-mono">22 of 25</div>
            <div className="text-[11px] text-emerald-400 mt-1">3 Supplementary Slots Open</div>
          </div>
        </div>
      </div>

      {/* Warnings & Feasibility Banner */}
      {simulation && simulation.warnings.length > 0 && (
        <div className="bg-amber-950/30 border border-amber-500/40 rounded-xl p-4 space-y-1">
          <div className="flex items-center gap-2 text-xs font-bold text-[#FABC4D] uppercase">
            <AlertTriangle className="w-4 h-4" />
            Tactical Ceiling Exceeded Warnings
          </div>
          {simulation.warnings.map((w: string, i: number) => (
            <div key={i} className="text-xs text-gray-300">
              • {w}
            </div>
          ))}
        </div>
      )}

      {remainingPurse < 0 && (
        <div className="bg-red-950/40 border border-red-500/50 rounded-xl p-4 flex items-center gap-3 text-xs text-red-300">
          <AlertTriangle className="w-5 h-5 text-red-400 shrink-0" />
          <div>
            <span className="font-bold">Budget Deficit: </span>
            Selected bidding amounts exceed total remaining purse by ₹{Math.abs(remainingPurse).toFixed(2)} Cr. Reduce individual ceilings to achieve a feasible auction plan.
          </div>
        </div>
      )}

      {/* Targeted Bidding Sliders & Cards */}
      <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5">
        <h3 className="text-sm font-bold text-white uppercase tracking-wider mb-4">
          Interactive Bid Ceilings Simulation
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {targets.map((target) => {
            const currentBid = bids[target.name] ?? target.suggested_ceiling_cr;
            const isExceeded = currentBid > target.suggested_ceiling_cr;

            return (
              <div 
                key={target.target_id}
                className={`bg-[#122131] border rounded-xl p-4 space-y-3 transition-all ${
                  isExceeded ? 'border-[#FABC4D]/50 shadow-sm' : 'border-white/10'
                }`}
              >
                <div className="flex items-start justify-between">
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="text-sm font-bold text-white">{target.name}</span>
                      <span className="text-[10px] px-2 py-0.5 rounded bg-white/5 text-gray-300">
                        {target.role}
                      </span>
                    </div>
                    <div className="text-[11px] text-gray-400 mt-0.5">
                      {target.team} · Base: ₹{target.base_price_lakh} Lakh · SSSI: {target.sssi_pct}%
                    </div>
                  </div>
                  <div className="text-right">
                    <span className="text-sm font-extrabold font-mono text-[#FABC4D]">
                      ₹{currentBid.toFixed(2)} Cr
                    </span>
                    <span className="text-[10px] text-gray-400 block">
                      Rec: ₹{target.suggested_ceiling_cr.toFixed(2)} Cr
                    </span>
                  </div>
                </div>

                {/* Slider */}
                <div>
                  <input
                    type="range"
                    min="1.0"
                    max={target.max_ceiling_cr}
                    step="0.1"
                    value={currentBid}
                    onChange={(e) => handleBidChange(target.name, parseFloat(e.target.value))}
                    className="w-full accent-[#EB107E] cursor-pointer"
                  />
                  <div className="flex justify-between text-[10px] font-mono text-gray-500 mt-1">
                    <span>Base (₹1.00 Cr)</span>
                    <span className="text-[#FABC4D]">Ceiling (₹{target.suggested_ceiling_cr.toFixed(2)} Cr)</span>
                    <span>Max (₹{target.max_ceiling_cr.toFixed(2)} Cr)</span>
                  </div>
                </div>

                {/* Key stats row */}
                <div className="pt-2 border-t border-white/5 flex items-center justify-between text-[11px] text-gray-300">
                  <span>Reliability Score: <strong className="text-white">{target.bpri_score || target.bowpri_score}</strong></span>
                  <span className="text-emerald-400 font-semibold">{target.eligibility}</span>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

