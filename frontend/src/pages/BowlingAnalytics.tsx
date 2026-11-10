import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api, Bowler } from '../services/api';
import { Search, ArrowUpDown, ChevronRight, Info, ShieldCheck, ShieldAlert } from 'lucide-react';

export const BowlingAnalytics: React.FC = () => {
  const navigate = useNavigate();
  const [bowlers, setBowlers] = useState<Bowler[]>([]);
  const [loading, setLoading] = useState(true);
  const [actionableOnly, setActionableOnly] = useState(true);
  const [search, setSearch] = useState('');
  const [sortBy, setSortBy] = useState('bowpri_score');
  const [ascending, setAscending] = useState(false);

  useEffect(() => {
    loadBowlers();
  }, [actionableOnly, sortBy, ascending]);

  const loadBowlers = () => {
    setLoading(true);
    api.getBowlers(actionableOnly, search || undefined, sortBy, ascending)
      .then(res => {
        setBowlers(res);
        setLoading(false);
      });
  };

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    loadBowlers();
  };

  const handleSort = (field: string) => {
    if (sortBy === field) {
      setAscending(!ascending);
    } else {
      setSortBy(field);
      setAscending(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Header and Controls */}
      <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="px-2.5 py-0.5 rounded bg-[#7BD0FF]/20 text-[#7BD0FF] text-[10px] font-bold uppercase">
              Audited Official Rankings
            </span>
            <span className="text-xs text-gray-400">SupeRR Selector Season 2</span>
          </div>
          <h2 className="text-xl font-bold text-white mt-1">Bowling Pressure Reliability Index (BOWPRI)</h2>
          <p className="text-xs text-gray-400 mt-0.5">
            Weights: 35% HP Economy (inv) + 25% HP Avg (inv) + 20% Death Econ (inv) + 10% Wickets/Ball + 10% Delta Econ.
          </p>
        </div>

        {/* Actionable / Benchmark Segregation Toggle */}
        <div className="flex flex-wrap items-center gap-3">
          <div className="flex items-center bg-[#122131] border border-white/10 rounded-lg p-1">
            <button
              onClick={() => setActionableOnly(true)}
              className={`px-3 py-1.5 rounded-md text-xs font-semibold flex items-center gap-1.5 transition-all ${
                actionableOnly
                  ? 'bg-[#EB107E] text-white shadow-sm'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              <ShieldCheck className="w-3.5 h-3.5" />
              Actionable (BCCI Eligible)
            </button>
            <button
              onClick={() => setActionableOnly(false)}
              className={`px-3 py-1.5 rounded-md text-xs font-semibold flex items-center gap-1.5 transition-all ${
                !actionableOnly
                  ? 'bg-[#1C2B3C] text-[#FABC4D] shadow-sm'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              <ShieldAlert className="w-3.5 h-3.5" />
              All Benchmark Bowlers
            </button>
          </div>

          {/* Search Bar */}
          <form onSubmit={handleSearch} className="relative">
            <Search className="w-3.5 h-3.5 text-gray-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="Search bowler or team..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="bg-[#122131] border border-white/10 rounded-lg pl-8 pr-3 py-1.5 text-xs text-white placeholder-gray-400 focus:outline-none focus:border-[#7BD0FF] w-48"
            />
          </form>
        </div>
      </div>

      {/* Bowlers Table */}
      <div className="bg-[#0D1C2D] border border-white/10 rounded-xl overflow-hidden shadow-xl">
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-[#122131] border-b border-white/10 text-[11px] font-bold text-gray-300 uppercase tracking-wider">
                <th className="py-3 px-4 w-12 text-center">Rank</th>
                <th className="py-3 px-4">Bowler / Franchise</th>
                <th 
                  className="py-3 px-4 cursor-pointer hover:text-white"
                  onClick={() => handleSort('bowpri_score')}
                >
                  <div className="flex items-center gap-1 text-[#7BD0FF]">
                    BOWPRI Score <ArrowUpDown className="w-3 h-3" />
                  </div>
                </th>
                <th 
                  className="py-3 px-4 cursor-pointer hover:text-white"
                  onClick={() => handleSort('pressure_economy_rate')}
                >
                  <div className="flex items-center gap-1">
                    HP Econ <ArrowUpDown className="w-3 h-3" />
                  </div>
                </th>
                <th 
                  className="py-3 px-4 cursor-pointer hover:text-white"
                  onClick={() => handleSort('pressure_bowling_avg')}
                >
                  <div className="flex items-center gap-1">
                    HP Avg <ArrowUpDown className="w-3 h-3" />
                  </div>
                </th>
                <th 
                  className="py-3 px-4 cursor-pointer hover:text-white"
                  onClick={() => handleSort('death_economy_rate')}
                >
                  <div className="flex items-center gap-1">
                    Death Econ <ArrowUpDown className="w-3 h-3" />
                  </div>
                </th>
                <th className="py-3 px-4">HP Wkts</th>
                <th 
                  className="py-3 px-4 cursor-pointer hover:text-white"
                  onClick={() => handleSort('sample_size_saturation_index_pct')}
                >
                  <div className="flex items-center gap-1">
                    SSSI % <ArrowUpDown className="w-3 h-3" />
                  </div>
                </th>
                <th className="py-3 px-4">95% Bootstrap CI</th>
                <th className="py-3 px-4">Auction Eligibility</th>
                <th className="py-3 px-4 text-center">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-white/5 text-xs">
              {loading ? (
                <tr>
                  <td colSpan={11} className="py-12 text-center text-gray-400">
                    <div className="inline-block animate-spin rounded-full h-6 w-6 border-b-2 border-[#7BD0FF]"></div>
                    <div className="mt-2 text-xs">Loading audited bowling records...</div>
                  </td>
                </tr>
              ) : bowlers.length === 0 ? (
                <tr>
                  <td colSpan={11} className="py-12 text-center text-gray-400">
                    No matching bowlers found for the specified filters.
                  </td>
                </tr>
              ) : (
                bowlers.map((b) => {
                  const isIneligible = b.ipl_auction_eligibility.toLowerCase().includes('ineligible');
                  return (
                    <tr 
                      key={b.player_id}
                      className="hover:bg-[#122131]/60 transition-colors group"
                    >
                      <td className="py-3.5 px-4 text-center">
                        <span className={`inline-flex items-center justify-center w-6 h-6 rounded-full font-mono text-xs font-bold ${
                          b.rank === 1 ? 'bg-[#7BD0FF] text-[#051424] font-extrabold shadow-md shadow-[#7BD0FF]/30' :
                          b.rank === 2 ? 'bg-[#FABC4D] text-[#051424] font-extrabold' :
                          b.rank === 3 ? 'bg-white text-[#051424] font-extrabold' :
                          'bg-white/5 text-gray-400'
                        }`}>
                          {b.rank}
                        </span>
                      </td>
                      <td className="py-3.5 px-4">
                        <div className="font-bold text-white group-hover:text-[#7BD0FF] transition-colors">
                          {b.player_name}
                        </div>
                        <div className="text-[11px] text-gray-400">{b.bowling_role} · {b.team}</div>
                      </td>
                      <td className="py-3.5 px-4 font-mono font-extrabold text-[#7BD0FF] text-sm">
                        {b.bowpri_score.toFixed(2)}
                      </td>
                      <td className="py-3.5 px-4 font-mono font-semibold text-white">
                        {b.pressure_economy_rate.toFixed(2)}
                      </td>
                      <td className="py-3.5 px-4 font-mono text-gray-300">
                        {b.pressure_bowling_avg.toFixed(1)}
                      </td>
                      <td className="py-3.5 px-4 font-mono font-semibold text-[#FABC4D]">
                        {b.death_economy_rate.toFixed(2)}
                      </td>
                      <td className="py-3.5 px-4 font-mono text-white">
                        {b.pressure_wickets}
                      </td>
                      <td className="py-3.5 px-4">
                        <div className="flex items-center gap-2">
                          <span className="font-mono text-white text-xs">{b.sample_size_saturation_index_pct.toFixed(0)}%</span>
                          <div className="w-12 bg-white/10 h-1.5 rounded-full overflow-hidden">
                            <div 
                              className="bg-[#7BD0FF] h-full rounded-full"
                              style={{ width: `${Math.min(100, b.sample_size_saturation_index_pct)}%` }}
                            ></div>
                          </div>
                        </div>
                      </td>
                      <td className="py-3.5 px-4 font-mono text-[11px] text-gray-300">
                        [{b.bootstrap_95_ci_lower_econ.toFixed(2)}, {b.bootstrap_95_ci_upper_econ.toFixed(2)}]
                      </td>
                      <td className="py-3.5 px-4">
                        <span className={`inline-flex items-center px-2 py-0.5 rounded text-[10px] font-bold ${
                          isIneligible
                            ? 'bg-red-950/60 text-red-300 border border-red-500/30'
                            : 'bg-emerald-950/60 text-emerald-300 border border-emerald-500/30'
                        }`}>
                          {b.ipl_auction_eligibility}
                        </span>
                      </td>
                      <td className="py-3.5 px-4 text-center">
                        <button
                          onClick={() => navigate(`/profiles?id=${b.player_id}`)}
                          className="px-2.5 py-1 rounded bg-[#1C2B3C] hover:bg-[#7BD0FF] hover:text-[#051424] text-white text-[11px] font-semibold transition-all flex items-center gap-1 mx-auto"
                        >
                          Profile <ChevronRight className="w-3 h-3" />
                        </button>
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Policy Notice Box */}
      <div className="bg-[#051424] border border-white/10 rounded-xl p-4 flex items-start gap-3 text-xs text-gray-400">
        <Info className="w-5 h-5 text-[#7BD0FF] shrink-0 mt-0.5" />
        <div>
          <span className="font-bold text-white">Regulatory Segregation Mandate: </span>
          Pakistani international cricketers (e.g. Mohammad Nawaz, Abrar Ahmed) are registered in the global dataset and provide non-parametric Bayesian prior calibrations for high-pressure death economy models. Under BCCI IPL governance rules, they are strictly <span className="text-red-400 font-bold">ineligible for auction bidding</span>. 
          Rajasthan Royals actionable scouting targets begin with <span className="text-[#7BD0FF] font-bold">Matthew Humphreys (BOWPRI 76.68)</span>, <span className="text-[#7BD0FF] font-bold">George Linde (BOWPRI 76.10)</span>, and <span className="text-[#7BD0FF] font-bold">Sunil Narine (BOWPRI 75.71)</span>.
        </div>
      </div>
    </div>
  );
};

