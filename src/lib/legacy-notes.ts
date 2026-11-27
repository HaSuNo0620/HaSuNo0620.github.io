// Canonical destinations for superseded notes. Source manuscripts remain in the repository.
export const legacyNotes: Record<string,string> = {
  "interface-thinking-map": "/fields/interfaces/",
  "spin-model-thinking-map": "/fields/statistical-physics/",
  "quasicrystal-order-without-periodicity": "/fields/quasicrystals/",
  "ising-rn-transfer-matrix": "/notes/finite-range-symmetry-comparison/",
  "clock-chain-finite-range": "/notes/finite-range-symmetry-comparison/",
  "xy-chain-finite-range": "/notes/finite-range-symmetry-comparison/",
  "ising-range-comparison": "/notes/finite-range-symmetry-comparison/",
  "ising-xy-nearest-neighbor-comparison": "/notes/clock-chain-nearest-neighbor/"
};
export const isLegacyNote=(id:string)=>Object.hasOwn(legacyNotes,id);
